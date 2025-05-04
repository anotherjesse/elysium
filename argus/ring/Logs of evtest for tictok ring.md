
The events are kinda funky because it simulates swiping up/down events:

| Physical action                            | HID Events                                                                                        |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| Scroll Wheel Up                            | `BTN_TOUCH`, then report different `ABS_Y` positions from top to bottom every 0.03s, then release |
| Scroll Wheel Down                          | same as Up but positions `ABS_Y` from bottom to top                                               |
| Button Press (after using Scroll Wheel)    | `BTN_TOUCH`, then report position to the center of the screen, then release                       |
| Button Press (after previous button press) | `BTN_TOUCH`, then release                                                                         |
| Volume Buttons                             | seem like normal `HID` events                                                                     |


My algorithm so far:
  - Watch for `BTN_TOUCH` to pressed, then collect `ABS_Y` value
  - Look at last `ABS_Y` value  during the `BTN_TOUCH` event below for 3 magic numbers:
    - `500`: scroll down
    - `3200`: scroll up
    - `1904`: button press
    - `None`: button press

## Scroll down

```
Event: time 1746371934.711869, type 4 (EV_MSC), code 4 (MSC_SCAN), value d0042
Event: time 1746371934.711869, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 1
Event: time 1746371934.711869, type 1 (EV_KEY), code 320 (BTN_TOOL_PEN), value 1
Event: time 1746371934.711869, type 3 (EV_ABS), code 1 (ABS_Y), value 3200
Event: time 1746371934.711869, -------------- SYN_REPORT ------------
Event: time 1746371934.714376, type 3 (EV_ABS), code 1 (ABS_Y), value 2600
Event: time 1746371934.714376, -------------- SYN_REPORT ------------
Event: time 1746371934.741873, type 3 (EV_ABS), code 1 (ABS_Y), value 2300
Event: time 1746371934.741873, -------------- SYN_REPORT ------------
Event: time 1746371934.771816, type 3 (EV_ABS), code 1 (ABS_Y), value 2000
Event: time 1746371934.771816, -------------- SYN_REPORT ------------
Event: time 1746371934.774363, type 3 (EV_ABS), code 1 (ABS_Y), value 1700
Event: time 1746371934.774363, -------------- SYN_REPORT ------------
Event: time 1746371934.801850, type 3 (EV_ABS), code 1 (ABS_Y), value 1400
Event: time 1746371934.801850, -------------- SYN_REPORT ------------
Event: time 1746371934.831816, type 3 (EV_ABS), code 1 (ABS_Y), value 1100
Event: time 1746371934.831816, -------------- SYN_REPORT ------------
Event: time 1746371934.834424, type 3 (EV_ABS), code 1 (ABS_Y), value 800
Event: time 1746371934.834424, -------------- SYN_REPORT ------------
Event: time 1746371934.861889, type 3 (EV_ABS), code 1 (ABS_Y), value 500
Event: time 1746371934.861889, -------------- SYN_REPORT ------------
Event: time 1746371934.891934, type 4 (EV_MSC), code 4 (MSC_SCAN), value d0042
Event: time 1746371934.891934, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 0
Event: time 1746371934.891934, type 1 (EV_KEY), code 320 (BTN_TOOL_PEN), value 0
Event: time 1746371934.891934, -------------- SYN_REPORT ------------
Event: time 1746371934.891942, type 3 (EV_ABS), code 1 (ABS_Y), value 200
Event: time 1746371934.891942, -------------- SYN_REPORT ------------
```

## Scroll up

```
Event: time 1746371959.493914, type 4 (EV_MSC), code 4 (MSC_SCAN), value d0042
Event: time 1746371959.493914, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 1
Event: time 1746371959.493914, type 1 (EV_KEY), code 320 (BTN_TOOL_PEN), value 1
Event: time 1746371959.493914, type 3 (EV_ABS), code 1 (ABS_Y), value 1012
Event: time 1746371959.493914, -------------- SYN_REPORT ------------
Event: time 1746371959.495106, type 3 (EV_ABS), code 1 (ABS_Y), value 1100
Event: time 1746371959.495106, -------------- SYN_REPORT ------------
Event: time 1746371959.523851, type 3 (EV_ABS), code 1 (ABS_Y), value 1400
Event: time 1746371959.523851, -------------- SYN_REPORT ------------
Event: time 1746371959.553803, type 3 (EV_ABS), code 1 (ABS_Y), value 1700
Event: time 1746371959.553803, -------------- SYN_REPORT ------------
Event: time 1746371959.555067, type 3 (EV_ABS), code 1 (ABS_Y), value 2000
Event: time 1746371959.555067, -------------- SYN_REPORT ------------
Event: time 1746371959.583736, type 3 (EV_ABS), code 1 (ABS_Y), value 2300
Event: time 1746371959.583736, -------------- SYN_REPORT ------------
Event: time 1746371959.612539, type 3 (EV_ABS), code 1 (ABS_Y), value 2600
Event: time 1746371959.612539, -------------- SYN_REPORT ------------
Event: time 1746371959.642606, type 3 (EV_ABS), code 1 (ABS_Y), value 2900
Event: time 1746371959.642606, -------------- SYN_REPORT ------------
Event: time 1746371959.643752, type 3 (EV_ABS), code 1 (ABS_Y), value 3200
Event: time 1746371959.643752, -------------- SYN_REPORT ------------
Event: time 1746371959.672603, type 4 (EV_MSC), code 4 (MSC_SCAN), value d0042
Event: time 1746371959.672603, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 0
Event: time 1746371959.672603, type 1 (EV_KEY), code 320 (BTN_TOOL_PEN), value 0
Event: time 1746371959.672603, -------------- SYN_REPORT ------------
Event: time 1746371959.672610, type 3 (EV_ABS), code 1 (ABS_Y), value 3500
Event: time 1746371959.672610, -------------- SYN_REPORT ------------
```

## Button press (first time)

```
Event: time 1746371995.464807, type 4 (EV_MSC), code 4 (MSC_SCAN), value d0042
Event: time 1746371995.464807, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 1
Event: time 1746371995.464807, type 1 (EV_KEY), code 320 (BTN_TOOL_PEN), value 1
Event: time 1746371995.464807, type 3 (EV_ABS), code 1 (ABS_Y), value 1904
Event: time 1746371995.464807, -------------- SYN_REPORT ------------
Event: time 1746371995.493550, type 4 (EV_MSC), code 4 (MSC_SCAN), value d0042
Event: time 1746371995.493550, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 0
Event: time 1746371995.493550, type 1 (EV_KEY), code 320 (BTN_TOOL_PEN), value 0
Event: time 1746371995.493550, -------------- SYN_REPORT ------------
```

## Button press (second time)

```
Event: time 1746372015.686640, type 4 (EV_MSC), code 4 (MSC_SCAN), value d0042
Event: time 1746372015.686640, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 1
Event: time 1746372015.686640, type 1 (EV_KEY), code 320 (BTN_TOOL_PEN), value 1
Event: time 1746372015.686640, -------------- SYN_REPORT ------------
Event: time 1746372015.714077, type 4 (EV_MSC), code 4 (MSC_SCAN), value d0042
Event: time 1746372015.714077, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 0
Event: time 1746372015.714077, type 1 (EV_KEY), code 320 (BTN_TOOL_PEN), value 0
Event: time 1746372015.714077, -------------- SYN_REPORT ------------
```

## Volume up

```
Event: time 1746372027.805602, type 4 (EV_MSC), code 4 (MSC_SCAN), value c00e9
Event: time 1746372027.805602, type 1 (EV_KEY), code 115 (KEY_VOLUMEUP), value 1
Event: time 1746372027.805602, -------------- SYN_REPORT ------------
Event: time 1746372027.835594, type 4 (EV_MSC), code 4 (MSC_SCAN), value c00e9
Event: time 1746372027.835594, type 1 (EV_KEY), code 115 (KEY_VOLUMEUP), value 0
Event: time 1746372027.835594, -------------- SYN_REPORT ------------
```

## Volume down

```
Event: time 1746372042.174768, type 4 (EV_MSC), code 4 (MSC_SCAN), value c00ea
Event: time 1746372042.174768, type 1 (EV_KEY), code 114 (KEY_VOLUMEDOWN), value 1
Event: time 1746372042.174768, -------------- SYN_REPORT ------------
Event: time 1746372042.177258, type 4 (EV_MSC), code 4 (MSC_SCAN), value c00ea
Event: time 1746372042.177258, type 1 (EV_KEY), code 114 (KEY_VOLUMEDOWN), value 0
Event: time 1746372042.177258, -------------- SYN_REPORT ------------
```