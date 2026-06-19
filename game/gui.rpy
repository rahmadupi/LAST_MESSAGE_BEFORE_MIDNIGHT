## gui.rpy
## Neubrutal style overrides for Last Message Before Midnight
## All visuals are drawn with widgets — no image assets required.

# ============================================================================
# Palette (kept here for reference / re-use)
# ============================================================================
#   outside  = #0a0a15   (near-black backdrop)
#   phone    = #1e1e2e   (dark phone body)
#   paper    = #ececf2   (light chat background)
#   ink      = #0f0f1a   (heavy borders, status bar)
#   text     = #101820   (text on bubbles)
#   green    = #95d3a4   (Alya bubble)
#   blue     = #7fb1e8   (Player bubble)
#   yellow   = #f4d03f   (Neubrutal accent)
#   hover    = #ffe873   (Button hover)
#   hint     = #5a5a6a   (subtle grey)
# ============================================================================

# ---------------------------------------------------------------------------
# Base frames
# ---------------------------------------------------------------------------
style lmbm_frame:
    background Solid("#0a0a15")
    padding (0, 0, 0, 0)

style lmbm_phone:
    background Solid("#1e1e2e")
    padding (10, 10, 10, 10)

style lmbm_phone_inner:
    background Solid("#d8d8e0")
    padding (0, 0, 0, 0)

# ---------------------------------------------------------------------------
# Status bar
# ---------------------------------------------------------------------------
style lmbm_statusbar:
    background Solid("#0f0f1a")
    padding (18, 10, 18, 10)
    ysize 44
    xfill True

style lmbm_statusbar_text:
    color "#ffffff"
    text_align 0.5
    yalign 0.5
    font "gui/font/DejaVuSans-Bold.ttf"
    size 18

style lmbm_chat_area:
    background Solid("#ececf2")
    padding (14, 12, 14, 12)
    xfill True
    yfill True

# ---------------------------------------------------------------------------
# Chat bubbles
# The 3px black border is added via a wrapper frame in screens.rpy
# (this style only handles background, padding, and text).
# ---------------------------------------------------------------------------
style lmbm_bubble_alya:
    background Solid("#95d3a4")
    padding (14, 10, 14, 10)
    yminimum 36
    xmaximum 440
    font "gui/font/DejaVuSans.ttf"
    size 19
    color "#101820"
    line_spacing 4
    text_align 0.0

style lmbm_bubble_player:
    background Solid("#7fb1e8")
    padding (14, 10, 14, 10)
    yminimum 36
    xmaximum 440
    font "gui/font/DejaVuSans.ttf"
    size 19
    color "#101820"
    line_spacing 4
    text_align 0.0

# Bubble border (used as wrapper around the colored bubble)
style lmbm_bubble_border:
    background Solid("#0f0f1a")
    padding (3, 3, 3, 3)

# ---------------------------------------------------------------------------
# Choice box (bracketed buttons at the bottom of the phone)
# ---------------------------------------------------------------------------
style lmbm_choice_box:
    background Solid("#1e1e2e")
    padding (14, 12, 14, 12)
    xfill True
    yminimum 110

style lmbm_choice_button:
    background Solid("#f4d03f")
    padding (12, 10, 12, 10)
    yminimum 44
    xfill True
    bottom_margin 8
    font "gui/font/DejaVuSans-Bold.ttf"
    size 18
    color "#0f0f1a"
    text_align 0.0
    insensitive_background Solid("#9b9b9b")
    hover_background Solid("#ffe873")

style lmbm_choice_label:
    text_align 0.0
    color "#0f0f1a"

# ---------------------------------------------------------------------------
# Main menu Play button
# ---------------------------------------------------------------------------
style lmbm_menu_button:
    background Solid("#f4d03f")
    padding (40, 22, 40, 22)
    yminimum 80
    xminimum 280
    font "gui/font/DejaVuSans-Bold.ttf"
    size 36
    color "#0f0f1a"
    text_align 0.5
    bottom_margin 14
    hover_background Solid("#ffe873")

style lmbm_play_btn:
    background Solid("#f4d03f")
    hover_background Solid("#ffe873")
    padding (40, 22, 40, 22)
    yminimum 60
    xminimum 200
    font "gui/font/DejaVuSans-Bold.ttf"
    size 32
    color "#0f0f1a"
    text_align 0.5

style lmbm_choice_button:
    background Solid("#f4d03f")
    hover_background Solid("#ffe873")
    padding (12, 10, 12, 10)
    yminimum 40
    xfill True
    font "gui/font/DejaVuSans-Bold.ttf"
    size 16
    color "#0f0f1a"
    text_align 0.0

style lmbm_menu_title:
    font "gui/font/DejaVuSans-Bold.ttf"
    size 56
    color "#f4d03f"
    text_align 0.5
    outlines [(4, "#0f0f1a", 0, 0)]
    bottom_margin 20

style lmbm_menu_subtitle:
    font "gui/font/DejaVuSans.ttf"
    size 22
    color "#ececf2"
    text_align 0.5
    outlines [(2, "#0f0f1a", 0, 0)]

# ---------------------------------------------------------------------------
# Misc
# ---------------------------------------------------------------------------
style lmbm_hint_text:
    font "gui/font/DejaVuSans.ttf"
    size 14
    color "#5a5a6a"
    text_align 0.5

style lmbm_offline_text:
    font "gui/font/DejaVuSans-Bold.ttf"
    size 18
    color "#7a7a85"
    text_align 0.5
    italic True

style lmbm_quickmenu_btn:
    background Solid("#1e1e2e")
    padding (10, 4, 10, 6)
    color "#f4d03f"
    size 18
    font "gui/font/DejaVuSans-Bold.ttf"
    hover_background Solid("#3a3a4e")
