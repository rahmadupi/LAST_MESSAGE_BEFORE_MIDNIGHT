## options.rpy
## Game configuration for Last Message Before Midnight
##
## Ren'Py 8.x compatible — only valid config variables are used.

## Window size — phone aspect ratio (9:16 portrait)
## The whole window IS the phone screen; no empty canvas around it.
init python:
    config.screen_width = 540
    config.screen_height = 960

    ## Skip / pacing
    config.allow_skipping = True
    config.skipping = False
    config.fast_skipping = True

## Game metadata
define config.name = "Last Message Before Midnight"
define config.version = "1.0"
define config.window_title = "Last Message Before Midnight"
