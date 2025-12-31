# bot.py
import os
from primekillermd import antidelete, antilink, group_commands, media, bug_crash, utils
from datetime import datetime

# Owner & channels
OWNER_NUMBER = "254792770219"
WHATSAPP_CHANNEL = "https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l"
TELEGRAM_CHANNEL = "https://t.me/primekillercrasher"
TELEGRAM_GROUP = "https://t.me/primekillercrasherv1"

# Initialize bot (example using utils.py init function)
bot = utils.init_bot(owner=OWNER_NUMBER)

# Menu function
def send_menu(user):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    menu_text = f"""
╭━━ ◇「 ° PRIME KILLER MD ° 」◇
┃⌬ ʙᴏᴛ : ⛧ＰＲＩΜΞ⛧ ᴋîᄂᄂér ⛧CЯΛSᕼΞЯ⛧
┃⌬ ᴜsᴇʀ : {user}
┃⌬ ᴘʟᴀᴛғᴏʀᴍ : ᴡʜᴀᴛsᴀᴘᴘ
┃⌬ ᴏᴡɴᴇʀ : +{OWNER_NUMBER}
┃⌬ ᴅᴇᴠ : Primekiller Kent
┃⌬ ᴅᴀᴛᴇ : {now}
╰━━━━━━━━━━━━━━━◇

╭━━ ◇「 ° COMMANDS ° 」◇
┃⌬ .pair - Connect device
┃⌬ .delpair - Remove device
┃⌬ .listpair - View all devices
┃⌬ .listmode - View connected modes
┃⌬ .runtime - View bot uptime
┃⌬ .antidelete - Anti delete messages
┃⌬ .antilink - Anti link protection
┃⌬ .promote - Promote member
┃⌬ .demote - Demote member
┃⌬ .kick - Kick member
┃⌬ .kickall - Kick all
┃⌬ .open - Open group
┃⌬ .close - Close group
┃⌬ .image - Download image
┃⌬ .song - Download song
┃⌬ .vcf - Download VCF contact
┃⌬ .video - Download video
┃⌬ .yts - YouTube search
┃⌬ .tiktok - TikTok download
┃⌬ .bugcrash - Bug Crash ⚠️ Coming Soon
┃⌬ .ping - Check bot status
╰━━━━━━━━━━━━━━━◇

View WhatsApp Channel: {WHATSAPP_CHANNEL}
Join Telegram Channel: {TELEGRAM_CHANNEL}
Join Telegram Group: {TELEGRAM_GROUP}
Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧
"""
    bot.send_message(user, menu_text, image="Prime_Killer_MD.png")

# Command handler
def handle_commands(user, message):
    text = message.lower()

    # Menu
    if text.startswith(".menu"):
        send_menu(user)

    # Ping
    elif text.startswith(".ping"):
        bot.send_message(user, "🏓 Pong! Bot is alive!")

    # Antidelete
    elif text.startswith(".antidelete"):
        antidelete.run(bot, user, WHATSAPP_CHANNEL)

    # Antilink
    elif text.startswith(".antilink"):
        antilink.run(bot, user, WHATSAPP_CHANNEL)

    # Group commands
    elif text.startswith((".promote", ".demote", ".kick", ".kickall", ".open", ".close")):
        group_commands.run(bot, user, text)

    # Media commands
    elif text.startswith((".image", ".song", ".vcf", ".video", ".yts", ".tiktok")):
        media.run(bot, user, text)

    # Bug crash
    elif text.startswith(".bugcrash"):
        bug_crash.run(bot, user)

    # Pair commands
    elif text.startswith((".pair", ".delpair", ".listpair")):
        utils.pair_command(bot, user, text)

# Welcome/start message
def start_message(user):
    message = f"""
⛧ＰＲＩΜΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ ɃЦ₲ ɃØŦ is running...
Owner: +{OWNER_NUMBER}
Join the channel first to use the bot: {WHATSAPP_CHANNEL}
Type .menu to see all commands.
"""
    bot.send_message(user, message)

# Main loop
def main():
    for user, message in bot.listen():  # listen() should yield (user, message)
        if message.startswith(".start"):
            start_message(user)
        else:
            handle_commands(user, message)

if __name__ == "__main__":
    print("⛧ＰＲＩΜΞ⛧ ᴋîᄂᄂér ⛧CЯΛSᕼΞЯ⛧ WhatsApp Bot is running...")
    main()
