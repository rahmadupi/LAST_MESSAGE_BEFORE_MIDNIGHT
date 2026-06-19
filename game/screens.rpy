## screens.rpy
## Last Message Before Midnight — custom UI screens.

# =============================================================================
# Status bar
# =============================================================================
screen lmbm_statusbar():
    frame:
        background Solid("#0f0f1a")
        xfill True
        ysize 44
        hbox:
            xfill True
            yfill True
            spacing 12
            text "<":
                color "#ffffff"
                size 22
                yalign 0.5
                font "gui/font/DejaVuSans-Bold.ttf"
            text "Chat":
                color "#ffffff"
                size 16
                yalign 0.5
                font "gui/font/DejaVuSans-Bold.ttf"
            null width 1 xfill True
            text "▮▮▮":
                color "#95d3a4"
                size 16
                yalign 0.5
                font "gui/font/DejaVuSans-Bold.ttf"
            text "[story_clock]":
                color "#ffffff"
                size 16
                yalign 0.5
                font "gui/font/DejaVuSans-Bold.ttf"

# =============================================================================
# Main menu
# =============================================================================
screen main_menu():
    tag menu

    frame:
        background Solid("#1e1e2e")
        xfill True
        yfill True

        frame:
            background Solid("#ececf2")
            xfill True
            yfill True

            vbox:
                xfill True
                yfill True
                spacing 0

                use lmbm_statusbar
                frame:
                    background Solid("#0f0f1a")
                    ysize 2
                    xfill True

                vbox:
                    xalign 0.5
                    yalign 0.5
                    xfill True
                    yfill True
                    spacing 16

                    text "LAST MESSAGE\nBEFORE MIDNIGHT":
                        font "gui/font/DejaVuSans-Bold.ttf"
                        size 36
                        color "#f4d03f"
                        text_align 0.5
                        xalign 0.5
                        outlines [(3, "#0f0f1a", 0, 0)]

                    text "a psychological visual novel":
                        font "gui/font/DejaVuSans.ttf"
                        size 16
                        color "#5a5a6a"
                        text_align 0.5
                        xalign 0.5

                    null height 24

                    frame:
                        background Solid("#0f0f1a")
                        padding (5, 5, 5, 5)
                        xalign 0.5
                        textbutton "PLAY":
                            style "lmbm_play_btn"
                            action Start()

                    null height 24

                    text "v1.0  •  rahmadupi  •  Ren'Py":
                        font "gui/font/DejaVuSans.ttf"
                        size 13
                        color "#7a7a85"
                        text_align 0.5
                        xalign 0.5

# =============================================================================
# NVL screen
# =============================================================================
screen nvl(dialogue, items=None):
    frame:
        background Solid("#1e1e2e")
        xfill True
        yfill True

        frame:
            background Solid("#ececf2")
            xfill True
            yfill True

            vbox:
                xfill True
                yfill True
                spacing 0

                use lmbm_statusbar
                frame:
                    background Solid("#0f0f1a")
                    ysize 2
                    xfill True

                # Chat area — simple vbox, no viewport
                vbox:
                    xfill True
                    yfill True
                    spacing 10

                    if nvl_list:
                        for entry in nvl_list:
                            if entry[0] == "Alya":
                                frame:
                                    background Solid("#95d3a4")
                                    padding (12, 8, 12, 8)
                                    xalign 0.0
                                    xmaximum 420
                                    text (entry[1]):
                                        font "gui/font/DejaVuSans.ttf"
                                        size 19
                                        color "#101820"
                                        text_align 0.0
                            else:
                                frame:
                                    background Solid("#7fb1e8")
                                    padding (12, 8, 12, 8)
                                    xalign 1.0
                                    xmaximum 420
                                    text (entry[1]):
                                        font "gui/font/DejaVuSans.ttf"
                                        size 19
                                        color "#101820"
                                        text_align 0.0
                    else:
                        text "no messages":
                            font "gui/font/DejaVuSans.ttf"
                            size 14
                            color "#5a5a6a"
                            xalign 0.5

    $ current_what = (nvl_list[-1][1] if nvl_list else "")
    text current_what id "what" xpos -1000 ypos -1000 color "#000"

# =============================================================================
# Choice screen
# =============================================================================
screen choice(items):
    frame:
        background Solid("#1e1e2e")
        xfill True
        yfill True

        frame:
            background Solid("#ececf2")
            xfill True
            yfill True

            vbox:
                xfill True
                yfill True
                spacing 0

                use lmbm_statusbar
                frame:
                    background Solid("#0f0f1a")
                    ysize 2
                    xfill True

                # Chat area
                vbox:
                    xfill True
                    yfill True
                    spacing 10
                    for entry in nvl_list:
                        if entry[0] == "Alya":
                            frame:
                                background Solid("#95d3a4")
                                padding (12, 8, 12, 8)
                                xalign 0.0
                                xmaximum 420
                                text (entry[1]):
                                    font "gui/font/DejaVuSans.ttf"
                                    size 19
                                    color "#101820"
                                    text_align 0.0
                        else:
                            frame:
                                background Solid("#7fb1e8")
                                padding (12, 8, 12, 8)
                                xalign 1.0
                                xmaximum 420
                                text (entry[1]):
                                    font "gui/font/DejaVuSans.ttf"
                                    size 19
                                    color "#101820"
                                    text_align 0.0

                # Choice box
                frame:
                    background Solid("#1e1e2e")
                    padding (12, 10, 12, 10)
                    xfill True
                    yminimum 110
                    vbox:
                        xfill True
                        spacing 6
                        for caption, action, chosen in items:
                            if chosen:
                                frame:
                                    background Solid("#cfcfd6")
                                    padding (10, 8, 10, 8)
                                    xfill True
                                    yminimum 40
                                    text caption:
                                        font "gui/font/DejaVuSans-Bold.ttf"
                                        size 16
                                        color "#6a6a75"
                                        text_align 0.0
                            else:
                                frame:
                                    background Solid("#0f0f1a")
                                    padding (3, 3, 3, 3)
                                    xfill True
                                    textbutton caption:
                                        style "lmbm_choice_button"
                                        action action

# =============================================================================
# Overlays
# =============================================================================
screen lmbm_offline_overlay():
    modal True
    zorder 200
    frame:
        background Solid("#0a0a15")
        xfill True
        yfill True
        frame:
            background Solid("#1e1e2e")
            xalign 0.5
            yalign 0.5
            xmaximum 420
            yminimum 180
            padding (24, 24, 24, 24)
            vbox:
                xfill True
                spacing 12
                text "(Alya is offline)":
                    font "gui/font/DejaVuSans-Bold.ttf"
                    size 22
                    color "#95d3a4"
                    text_align 0.5
                frame:
                    background Solid("#0f0f1a")
                    ysize 2
                    xfill True
                text "This number is no longer active.":
                    font "gui/font/DejaVuSans.ttf"
                    size 16
                    color "#cfcfd6"
                    text_align 0.5
                null height 8
                text "Klik untuk lanjut...":
                    font "gui/font/DejaVuSans.ttf"
                    size 14
                    color "#7a7a85"
                    text_align 0.5

screen lmbm_connection_overlay():
    modal True
    zorder 200
    frame:
        background Solid("#0a0a15")
        xfill True
        yfill True
        frame:
            background Solid("#1e1e2e")
            xalign 0.5
            yalign 0.5
            xmaximum 420
            yminimum 200
            padding (24, 24, 24, 24)
            vbox:
                xfill True
                spacing 12
                text "Connection Lost":
                    font "gui/font/DejaVuSans-Bold.ttf"
                    size 22
                    color "#ff7a7a"
                    text_align 0.5
                frame:
                    background Solid("#0f0f1a")
                    ysize 2
                    xfill True
                text "Connecting...":
                    font "gui/font/DejaVuSans.ttf"
                    size 16
                    color "#cfcfd6"
                    text_align 0.5
                null height 8
                text "Klik untuk lanjut...":
                    font "gui/font/DejaVuSans.ttf"
                    size 14
                    color "#7a7a85"
                    text_align 0.5

# =============================================================================
# Credits
# =============================================================================
screen lmbm_credits():
    modal True
    zorder 300
    frame:
        background Solid("#0a0a15")
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 14
            text "Last Message Before Midnight":
                font "gui/font/DejaVuSans-Bold.ttf"
                size 28
                color "#f4d03f"
                text_align 0.5
                outlines [(3, "#0f0f1a", 0, 0)]
            text "— end of conversation —":
                font "gui/font/DejaVuSans.ttf"
                size 14
                color "#7a7a85"
                text_align 0.5
            null height 8
            frame:
                background Solid("#0f0f1a")
                ysize 2
                xfill True
                xmaximum 280
            null height 8
            text "rahmadupi":
                font "gui/font/DejaVuSans-Bold.ttf"
                size 18
                color "#95d3a4"
                text_align 0.5
            null height 14
            text "Engine: Ren'Py":
                font "gui/font/DejaVuSans.ttf"
                size 13
                color "#7a7a85"
                text_align 0.5
            text "UI style: Neubrutal":
                font "gui/font/DejaVuSans.ttf"
                size 13
                color "#7a7a85"
                text_align 0.5
            null height 20
            frame:
                background Solid("#0f0f1a")
                padding (4, 4, 4, 4)
                xalign 0.5
                textbutton "Main Menu":
                    style "lmbm_play_btn"
                    action [Hide("lmbm_credits"), MainMenu()]

# =============================================================================
# Standard Ren'Py screens
# =============================================================================
screen save():
    tag file
    modal True
    frame:
        background Solid("#0a0a15")
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 16
            text "Save / Load is disabled for this demo.":
                font "gui/font/DejaVuSans.ttf"
                size 16
                color "#cfcfd6"
                text_align 0.5
            textbutton "Kembali":
                style "lmbm_play_btn"
                action Return()

screen load():
    tag file
    modal True
    use save

screen preferences():
    tag pref
    modal True
    frame:
        background Solid("#0a0a15")
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 16
            text "Preferences (tidak tersedia di demo).":
                font "gui/font/DejaVuSans.ttf"
                size 16
                color "#cfcfd6"
                text_align 0.5
            textbutton "Kembali":
                style "lmbm_play_btn"
                action Return()

screen yesno_prompt(message, yes_action, no_action):
    modal True
    frame:
        background Solid("#0a0a15")
        xfill True
        yfill True
        frame:
            background Solid("#1e1e2e")
            xalign 0.5
            yalign 0.5
            xmaximum 420
            padding (20, 20, 20, 20)
        vbox:
            xalign 0.5
            yalign 0.5
            xfill True
            spacing 16
            text message:
                font "gui/font/DejaVuSans-Bold.ttf"
                size 18
                color "#f4d03f"
                text_align 0.5
                outlines [(2, "#0f0f1a", 0, 0)]
                xfill True
            hbox:
                xalign 0.5
                spacing 12
                textbutton "Ya":
                    style "lmbm_play_btn"
                    action yes_action
                textbutton "Tidak":
                    style "lmbm_play_btn"
                    action no_action

screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu
    modal True
    frame:
        background Solid("#0a0a15")
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 14
            text title:
                font "gui/font/DejaVuSans-Bold.ttf"
                size 26
                color "#f4d03f"
                text_align 0.5
                outlines [(3, "#0f0f1a", 0, 0)]
            textbutton "Lanjutkan":
                style "lmbm_play_btn"
                action Return()
                xalign 0.5
            textbutton "Main Menu":
                style "lmbm_play_btn"
                action MainMenu()
                xalign 0.5
            textbutton "Keluar":
                style "lmbm_play_btn"
                action Quit(confirm=True)
                xalign 0.5
