## Use-Case: watching/listening to lectures/podcasts and taking notes

- scroll up/down - to go forward/backward 30s in the video
- button press - pause/play
- volume up - start/finish recording audio notes (timestamped)
- volume down - toggle between full screen and showing it in a small floating window and making everything else clear (eg, sunglasses mode, eg, taking a long walk)

## Implementation:

Currently I'm testing with mpv + i3 + evdev (eg, a custom python script that talks to other programs via ipc)

Everything is hardcoded for my setup and might not even survive the next reboot...

## Usage:

For initial testing, I'm manually starting mpv with the following command:

- FIXME(ja): For some reason, I have to use the deprecated `vo=x11` option, as wayland isn't working on the Khadas Edge2 ... Or something like that.

```
mpv lecture.webm --vo=x11 --input-ipc-server=/tmp/mpv-socket --idle=yes --ontop --no-border --autofit=no
```

and in another terminal I run the python script:

```
python3 experiment.py
```

Then I move the video window to an empty i3 workspace.

Now I can jump around the video, and stop it to record audio notes (to be transcribed/uploaded to Hephaestus)...

