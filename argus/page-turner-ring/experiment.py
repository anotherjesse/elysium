#!/usr/bin/env python3
import json
import socket
from evdev import InputDevice, ecodes
import i3ipc
from datetime import datetime
import subprocess
i3 = i3ipc.Connection()

def place_mpv(pct=0.2):
    """
    Moves the focused mpv window to (x,y) in pixels,
    then resizes it to w_pct% by h_pct% of the screen.
    """
    global screen_w, screen_h
    i3.command('floating enable')
    x = int(screen_w - screen_w * (pct))
    y = 0 #int(screen_h - screen_h * pct)
    i3.command(f'move window to position {x} {y}')
    root = i3.get_tree()
    w_px = int(root.rect.width * pct)
    h_px = int(root.rect.height * pct)
    i3.command(f'resize set {w_px} px {h_px} px')

SOCKET_PATH = '/tmp/mpv-socket'
dev = InputDevice('/dev/input/event12')

def send(cmd_list):
    msg = json.dumps({ 'command': cmd_list }) + '\n'
    try:
        with socket.socket(socket.AF_UNIX) as s:
            s.connect(SOCKET_PATH)
            s.send(msg.encode('utf-8'))
    except Exception as e:
        print("mpv IPC error:", e)


def notify(text, icon=None, timeout_ms=2000):
    """Send a desktop notification via notify-send."""
    cmd = ['notify-send', text, '-t', str(timeout_ms)]
    if icon:
        cmd.append('-i')
        cmd.append(icon)
    subprocess.run(cmd)

touching = False
last_y = None
last_scale = 100
recording = False

for ev in dev.read_loop():
    # start of a “touch” gesture
    if ev.type == ecodes.EV_KEY and ev.code == ecodes.BTN_TOUCH:
        if ev.value == 1:
            touching = True
            last_y = None
        else:  # ev.value == 0 → finger lifted
            touching = False
            # decide based on last_y
            if last_y is None or last_y == 1904:
                send(["cycle", "pause"])
            elif last_y == 3200:
                send(["seek", -30, "relative"])
            elif last_y == 500:
                send(["seek", 30, "relative"])
            last_y = None

    # while touching, record any ABS_Y
    elif touching and ev.type == ecodes.EV_ABS and ev.code == ecodes.ABS_Y:
        last_y = ev.value

    # volume keys can still go via IPC if you like:
    elif ev.type == ecodes.EV_KEY and ev.code == ecodes.KEY_VOLUMEDOWN and ev.value == 1:
        # send(["add", "volume", "-5"])
        if last_scale == 100:
            place_mpv(0.2)
            last_scale = 20
        else:
            place_mpv(1.0)
            last_scale = 100
    elif ev.type == ecodes.EV_KEY and ev.code == ecodes.KEY_VOLUMEUP   and ev.value == 1:
        if not recording:
            # start recording
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            record_filename = f"{timestamp}.wav"
            record_proc = subprocess.Popen([
                'pw-record', '--target', 'bluez_input.14_14_7D_E4_63_74.0', record_filename
            ])
            recording = True
            notify(f"Recording", "/usr/share/icons/elementary-xfce/devices/24/audio-input-microphone.png")
        else:
            # stop recording
            record_proc.terminate()
            record_proc.wait()
            recording = False
            notify(f"Saveed", "/usr/share/icons/elementary-xfce/actions/24/selection-checked.png")
