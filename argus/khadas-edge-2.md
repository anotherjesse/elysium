# Khadas Edge 2

## Fan in "pro" version

- goes off and on non-stop reagardless of what is happening... and is small therefore really noisy

## Battery

Requires a very specific USBC PD profile, otherwise it will continuously reboot.

## First setup

You have to set it up with HDMI - the USB-C DP only works after you are using linux.

## Graphics

The kernel driver / graphics support has some issues...

### Sway

I can't get `sway` window manger to work (even though the default unity desktop uses wayland)

### Failures to reconnect to USBC DP

Unplugging and plugging the USBC DP can cause the screen stop working :(

`dmesg` is spammed with:

```
[10108.160958] dw-dp fde50000.dp: video fifo overflow stream0
[10113.164223] dw_dp_irq_handler: 1482683 callbacks suppressed
```

## Linux

### shutdown hangs for 90s on...

```
Job session-49.scope/stop running (43s / 1min 30s)
```

### Audio

There are built-in microphones, but they are so close to the fans that all they pick up is noise.

To connect my airpods, I have to fiddle with bluetooth settings...

```
pactl set-card-profile bluez_card.14_14_7D_E4_63_74 headset-head-unit
```

Then I can record audio from my airpods with:

```
pw-record --target bluez_input.14_14_7D_E4_63_74.0 airpods.wav
```
