# bot.py
# Prime Killer MD WhatsApp Bot
# Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧

from primekillermd import (
    utils,
    antidelete,
    antilink,
    group_commands,
    media,
    bug_crash
)

# =========================
# BOT START MESSAGE (PANEL)
# =========================
utils.log_status(
    "⛧ＰＲＩΜΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ MD is ONLINE\n"
    "Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧\n\n"
    "Enter your phone number to pair  eg 2547xxxxxxx\n"
    "Then use:\n.pair PRIMEMD1"
)


# =========================
# MAIN MESSAGE HANDLER
# =========================
def on_message(message):
    """
    This function is called automatically by the WhatsApp runtime
    whenever a message is received.
    """

    sender = message.sender
    text = message.text.strip()
    chat = message.chat

    # Log message to panel
    utils.log_whatsapp_message(sender, chat, text)

    # =========================
    # PAIRING COMMANDS
    # =========================
    if text.startswith(".pair"):
        utils.pair_command(message)
        return

    if text.startswith(".delpair"):
        utils.delpair_command(message)
        return

    if text.startswith(".listpair"):
        utils.listpair_command(message)
        return

    # =========================
    # ACCESS CONTROL
    # =========================
    if not utils.check_access(message):
        return

    # =========================
    # MENU
    # =========================
    if text in [".menu", ".help"]:
        message.reply(
            "╭━━ ◇「 ⛧ＰＲＩΜΞ⛧ KILLER MD 」◇\n"
            "┃ Owner : 254792770219\n"
            "┃ Platform : WhatsApp\n"
            "┃ Status : Online\n"
            "╰━━━━━━━━━━━━━━━◇\n\n"

            "╭━━ ◇「 GROUP COMMANDS 」◇\n"
            "┃ .antilink on/off\n"
            "┃ .antidelete on/off\n"
            "┃ .promote @user\n"
            "┃ .demote @user\n"
            "┃ .kick @user\n"
            "┃ .kickall\n"
            "┃ .open / .close\n"
            "╰━━━━━━━━━━━━━━━◇\n\n"

            "╭━━ ◇「 MEDIA COMMANDS 」◇\n"
            "┃ .image <query>\n"
            "┃ .video <query>\n"
            "┃ .song <query>\n"
            "┃ .tiktok <link>\n"
            "┃ .yts <query>\n"
            "┃ .vcf\n"
            "╰━━━━━━━━━━━━━━━◇\n\n"

            "╭━━ ◇「 UTILITIES 」◇\n"
            "┃ .ping\n"
            "╰━━━━━━━━━━━━━━━◇\n\n"

            "╭━━ ◇「 BUG CRASH 」◇\n"
            "┃ ⚠ COMING SOON ⚠\n"
            "╰━━━━━━━━━━━━━━━◇\n\n"

            "🔗 WhatsApp Channel:\n"
            "https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l\n\n"

            "🔗 Telegram:\n"
            "https://t.me/primekillercrasher\n"
            "https://t.me/primekillercrasherv1\n\n"

            "Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧"
        )
        return

    # =========================
    # PING
    # =========================
    if text == ".ping":
        utils.ping(message)
        return

    # =========================
    # GROUP COMMANDS
    # =========================
    if text.startswith((
        ".antilink", ".antidelete",
        ".promote", ".demote",
        ".kick", ".kickall",
        ".open", ".close"
    )):
        group_commands.run(message)
        return

    # =========================
    # MEDIA COMMANDS
    # =========================
    if text.startswith((
        ".image", ".video", ".song",
        ".tiktok", ".yts", ".vcf"
    )):
        media.run(message)
        return

    # =========================
    # BUG CRASH (COMING SOON)
    # =========================
    if text.startswith(".bug"):
        bug_crash.run(message)
        return
