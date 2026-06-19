# Last Message Before Midnight

> _A chat-based psychological visual novel._
> Kamu menerima pesan dari teman yang seharusnya sudah tidak bisa menghubungimu lagi.

## Genre

Visual Novel / Psychological Mystery — built with **Ren'Py**.

## Premise

Alya, your research partner, died in a hit-and-run accident months ago. Tonight, her name pops up on your phone at 23:45. The clock on her side is stuck at 23:55. She's trapped between life and death in a loop, and only you can help her let go before midnight.

## How to Run

You need [Ren'Py 8.x](https://www.renpy.org/) installed.

```bash
# From the project root
renpy .
```

Or open the project in the Ren'Py launcher.

### Controls

- **Click / Enter / Space** — advance chat
- **Mouse wheel** — scroll through chat history
- **ESC** — pause / game menu
- **Tab** — toggle skip mode (auto-advance)
- **≡ button** (top right) — quick menure

## Project Layout

```
LAST_MESSAGE_BEFORE_MIDNIGHT/
├── README.md                  ← you are here
├── LICENSE
├── GDD/
│   ├── Last Message Before Midnight - GDD - Game Engine(T).txt
│   └── script.txt             ← original source dialogue
└── game/
    ├── options.rpy            ← engine configuration
    ├── gui.rpy                ← neubrutal style overrides
    ├── screens.rpy            ← phone UI, bubbles, menus, overlays
    ├── script.rpy             ← story + branching logic
    └── images/                ← (empty — all visuals are widgets)
```

## Story Structure

| Act | Title     | Mood        | Key beat                            |
| --- | --------- | ----------- | ----------------------------------- |
| 1   | Normal    | Casual      | Alya opens chat with small oddities |
| 2   | Uneasy    | Suspenseful | Clock stuck at 23:55, eerie silence |
| 3   | Memory    | Nostalgic   | The lab argument → the car accident |
| 4   | Breakdown | Panic       | Time-loop reveal                    |
| 5   | Midnight  | Emotional   | The final choice                    |

### Choices

1. **Act 1** — `Supportive` / `Dismissive` _(cosmetic; both branches continue)_
2. **Act 4** — `Comfort` / `Reject` _(cosmetic; both branches continue)_
3. **Act 5** — `Let Go` / `Stay` _(final — determines ending)_

### Endings

- **Good (Let Go)** — Alya finds peace. Phone number goes inactive.
- **Bad (Stay)** — Alya remains trapped. The loop restarts.
