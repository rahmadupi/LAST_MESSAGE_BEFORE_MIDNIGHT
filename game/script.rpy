## script.rpy
## Last Message Before Midnight
## A chat-based psychological visual novel.
##
## Flow:
##   start -> act1 -> [choice 1: supportive / dismissive]
##                  -> act2 -> act3 -> act4 -> [choice 2: comfort / reject]
##                                          -> act5 -> [final choice: let go / stay]
##                                                     -> good_ending / bad_ending

# ============================================================================
# Characters
# ============================================================================
# a   = Alya (green left bubble)
# p   = Player "Kamu" (blue right bubble)  — used sparingly, mostly for the
#                                              two early-choice replies and the
#                                              final choice, since the player
#                                              only "speaks" through choices.

## Alya uses NVL mode so chat history accumulates and shows on the phone
## screen as a scrollable thread, like a real messenger. Any non-Alya entry
## in nvl_list (e.g. the player's selected menu option) is rendered as a
## right-aligned blue bubble in the chat screen.
define a = Character("Alya", kind=nvl, who_color="#0f0f1a", what_color="#101820")

# Track branching choices (purely cosmetic; both early choices still lead
# to the same Act 2 onward, as per the GDD's "tidak mempengaruhi ending" rule).
default act1_choice = None    # "supportive" or "dismissive"
default act4_choice = None    # "comfort" or "reject"
default final_choice = None   # "letgo" or "stay"
default story_phase = "act1"

# ============================================================================
# Helpers
# ============================================================================
init python:
    def lmbm_pause(t=0.6):
        """A short beat between chat messages for pacing."""
        renpy.pause(t, hard=True)

    def lmbm_typing(t=1.0):
        """Simulate the 'Alya is typing…' indicator."""
        renpy.pause(t, hard=True)

    def lmbm_show_credits():
        """Display the end-credits screen and return to main menu."""
        renpy.show_screen("lmbm_credits")
        renpy.pause(hard=True)

# ============================================================================
# Status bar / clock text
# ============================================================================
# We track the in-story clock so the phone status bar updates with each act.
default story_clock = "23:45"

# ============================================================================
# ACT 1 — NORMAL
# ============================================================================
label start:
    $ story_phase = "act1"
    $ story_clock = "23:45"
    $ renpy.block_rollback()
    # Activate NVL mode so messages accumulate into the chat viewport.
    nvl show
    pause 0.3

    # Alya: casual opener. Small oddities (mentions "telat balas" early,
    # references things that haven't happened yet).
    a "hey…"
    $ lmbm_typing(0.5)
    a "kamu masih bangun kan?"
    $ lmbm_typing(0.5)
    a "tau ini udah malem banget."
    a "jam 2 pagi malah."
    a "pasti kamu masih di depan laptop."
    a "maaf ya kalau ganggu fokus kamu."
    a "tapi… aku ga tau harus chat siapa lagi."
    a "dadaku rasanya sesak banget."

    # ---- CHOICE 1 ----
    menu act1_menu:
        "kenapa al? tumben jam segini. aku belum tidur kok, baru aja kelar ngerjain project.":
            $ act1_choice = "supportive"
            jump act1_supportive
        "tidur al. besok aja ceritanya, aku udah capek banget mau istirahat.":
            $ act1_choice = "dismissive"
            jump act1_dismissive

label act1_supportive:
    a "syukurlah…"
    a "makasih udah mau nyempetin bales."
    a "aku tau kamu pasti capek habis mikirin error di kodenya."
    a "aku ganggu ya?"
    jump act1_continue

label act1_dismissive:
    a "tunggu…"
    a "bentar aja."
    a "tolong jangan dimatiin dulu hp-nya."
    a "aku mohon… ini beneran penting."
    a "aku butuh kamu."
    jump act1_continue

label act1_continue:
    a "aku ngerasa aneh banget hari ini."
    a "dari tadi sore…"
    a "atau dari kemarin ya?"
    a "pokoknya kayak… ada yang salah."
    a "aku ngerasa berat."
    a "padahal aku cuma tiduran aja di kasur."

# ============================================================================
# ACT 2 — UNEASY
# ============================================================================
label act2:
    $ story_phase = "act2"
    $ story_clock = "23:52"
    $ lmbm_pause(0.8)
    a "kamu mau ngetik \"sakit apa\", kan?"
    a "ga tau kenapa… aku bisa tau apa yang mau kamu bales."
    a "persis sebelum kamu ngetik."
    a "aneh ya?"
    a "hahah…"

    a "tapi ada yang lebih aneh lagi."
    a "jam di kamarku."
    a "dari tadi ga berubah."
    a "berhenti di 23:55."
    a "padahal perasaan kita udah chat lumayan lama…"
    a "batre hp-ku juga tetep 14%. ga turun-turun."

    a "dan di sini dingin banget."
    a "sepi."
    a "bener-bener ga ada suara apa-apa dari luar."
    a "biasanya jam segini masih ada suara motor lewat di depan kosan."
    a "atau suara jangkrik."
    a "tapi ini senyap."
    a "senyap yang bikin telinga penging."

    a "aku buka jendela, di luar gelap gulita."
    a "kayak ga ada kehidupan."
    a "aku cuma bisa liat layar hp ini."
    a "dan chat dari kamu."

# ============================================================================
# ACT 3 — MEMORY
# ============================================================================
label act3:
    $ story_phase = "act3"
    $ story_clock = "23:55"
    $ lmbm_pause(1.0)
    a "kamu inget ga…"
    a "malam itu?"
    a "pas hujan deres banget."
    a "kita lagi pusing-pusingnya ngurusin riset itu."
    a "kamu capek, aku juga capek karena revisi paper ga kelar-kelar."
    a "terus kita berantem hebat di lab."

    a "aku marah banget sama kamu…"
    a "aku bilang hal-hal yang jahat."
    a "aku bilang aku nyesel satu tim sama kamu."
    a "padahal aku ga pernah maksud gitu."
    a "aku cuma… stress."

    a "sampe akhirnya aku milih pergi."
    a "aku lari keluar kampus."
    a "kamu sempet teriak nyuruh aku nunggu hujan reda."
    a "tapi aku ga peduli."
    a "jalanan licin dan gelap banget malam itu."

    a "aku jalan sambil nangis."
    a "terus…"
    a "dari arah tikungan…"
    a "aku inget ada lampu mobil yang terang banget."
    a "nyorot langsung ke mataku."
    a "suara klakson yang panjang… decit ban…"
    a "terus…"
    a "semuanya hilang."

    a "abis itu cuma ada gelap."

# ============================================================================
# ACT 4 — BREAKDOWN
# ============================================================================
label act4:
    $ story_phase = "act4"
    $ story_clock = "23:55"   # stuck
    $ lmbm_pause(0.6)
    a "tunggu."
    a "kepalaku pusing."
    a "aku…"
    a "aku udah pernah ngetik ini kan?"
    a "iya kan?!"
    a "kemarin? atau besok?"
    a "kenapa kerasa berulang?!"

    a "ya ampun…"
    a "aku inget sekarang."
    a "aku udah minta maaf ke kamu berulang kali."
    a "tapi kenapa aku selalu balik lagi ke jam 23:55?!"
    a "kenapa aku masih di sini?!"

    a "dingin."
    a "dingin banget."
    a "aku ngerasain aspalnya lagi."
    a "air hujannya…"
    a "sakit. dadaku sakit banget."
    a "darahnya ga mau berhenti."
    a "tolong aku. aku takut."
    a "aku gamau mati sendirian di jalan ini!"

    # ---- CHOICE 2 ----
    menu act4_menu:
        "Alya, aku di sini. fokus ke chat aku. jangan inget-inget yang lain. tarik napas pelan-pelan.":
            $ act4_choice = "comfort"
            jump act4_comfort
        "Al, sumpah kamu ngomong apa sih? kamu di kosan kan sekarang? jangan bikin aku merinding.":
            $ act4_choice = "reject"
            jump act4_reject

label act4_comfort:
    a "makasih…"
    a "makasih udah nemenin aku."
    a "suara hujan di kepalaku pelan-pelan ilang kalau aku fokus ke layar ini."
    a "cuma kamu yang bikin aku ngerasa nyata."
    jump act4_continue

label act4_reject:
    a "tolong percaya sama aku!"
    a "jangan marah…"
    a "tolong jangan ngebentak aku lagi kayak malam di lab itu."
    a "aku cuma bingung… dan takut."
    jump act4_continue

label act4_continue:
    $ lmbm_pause(0.8)

# ============================================================================
# ACT 5 — MIDNIGHT
# ============================================================================
label act5:
    $ story_phase = "act5"
    $ story_clock = "23:58"
    a "jamnya gerak lagi."
    a "23:58."
    a "sebentar lagi 23:59."
    a "aku ngerasa… ini beneran waktunya."
    a "udara di sekitarku makin tipis."
    a "aku ngerasa badanku makin transparan."
    a "atau mungkin… aku emang udah ga ada dari malam itu?"
    a "dan ini cuma sisa-sisa kesadaranku aja."

    a "waktu kerasa cepet banget sekarang."
    a "aku gamau ngulang loop ini lagi."
    a "rasanya sakit banget tiap kali ketabrak lagi di ingatanku."

    a "dengerin aku ya."
    a "maafin aku buat semuanya."
    a "buat kata-kata kasarku di lab."
    a "buat ninggalin kamu gitu aja tanpa dengerin penjelasan kamu."
    a "buat ninggalin project kita."
    a "dan buat rasa bersalah yang harus kamu tanggung karena mikir ini salahmu."

    a "ini bukan salahmu."

    a "aku capek nahan beban ini sendirian di sini…"
    a "aku cuma butuh satu jawaban dari kamu."
    a "sebelum jam ini nyentuh jam 12."
    a "apa kamu… udah maafin aku?"

    # ---- FINAL CHOICE ----
    menu act5_menu:
        "aku udah maafin kamu dari lama, Al. itu bukan salah siapa-siapa. sekarang kamu boleh istirahat dengan tenang.":
            $ final_choice = "letgo"
            jump good_ending
        "jangan pergi Al! aku belum siap! aku masih butuh kamu buat semuanya. tolong jangan tinggalin aku lagi!":
            $ final_choice = "stay"
            jump bad_ending

# ============================================================================
# GOOD ENDING — Let Go
# ============================================================================
label good_ending:
    $ story_phase = "ending_good"
    $ story_clock = "23:59"
    a "benarkah…?"
    a "kamu ga benci aku?"
    a "…syukurlah."
    a "tiba-tiba… rasanya ga terlalu dingin lagi."
    a "rasa sakit di dadaku juga hilang."
    a "ada cahaya dari luar jendelaku."
    a "terang banget… tapi hangat."
    a "rasanya damai."
    a "akhirnya… aku bisa tidur."
    a "makasih ya, untuk semuanya."
    a "jangan lupa makan yang bener, jangan ngoding sampe pagi terus."
    a "selamat tinggal, temanku."

    $ lmbm_pause(1.5)
    # In-story offline indicator
    show screen lmbm_offline_overlay
    pause 2.0
    hide screen lmbm_offline_overlay
    pause 1.0

    # Roll credits
    $ lmbm_show_credits()
    return

# ============================================================================
# BAD ENDING — Stay (loops back to Act 1)
# ============================================================================
label bad_ending:
    $ story_phase = "ending_bad"
    $ story_clock = "23:59"
    a "tapi…"
    a "rasanya sakit kalau aku harus nahan diri di sini terus."
    a "kenapa kamu ga bisa ngelepasin aku?"
    a "kamu… kamu nahan aku buat pergi?"
    a "kenapa kamu egois?!"
    a "kamu mau aku ngerasain aspal dingin ini terus-terusan?!"
    a "dingin."
    a "dingin banget."
    a "semuanya gelap…"
    a "lampunya dateng lagi…"
    a "jamnya…"
    a "kenapa mundur lagi ke 23:55?!"
    a "sakit…"
    a "tolong… lepaskan aku…"

    $ lmbm_pause(1.5)
    show screen lmbm_connection_overlay
    pause 2.5
    hide screen lmbm_connection_overlay
    pause 1.0

    # Loop back to start — Alya's opening line echoes as the cycle restarts
    jump start

# ============================================================================
# Credits
# ============================================================================
init python:
    def lmbm_show_credits():
        """Show a simple end-credits screen and wait for click/enter."""
        renpy.show_screen("lmbm_credits")
        renpy.pause(hard=True)

## Reached after the player closes the credits screen.
label lmbm_credits_done:
    return
