# bot.py
import os
from primekillermd import antidelete, antilink, group_commands, media, bug_crash, utils

# Your bot details
BOT_NAME = "Prime Killer MD"
WHATSAPP_CHANNEL = "https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l"
OWNER_NUMBER = "254792770219"
TELEGRAM_CONTACT = "https://t.me/Handsome_primis_killer_kent"

# Initialize bot (example using a WhatsApp library)
bot = utils.init_bot(owner=OWNER_NUMBER)

# Menu / info message
def start_message(user):
    menu = f"""
╭━━ ◇「 ° INFOBOT ° 」◇
┃⌬ ʙᴏᴛ : {BOT_NAME}
┃⌬ ᴜsᴇʀ : {user}
┃⌬ ᴘʟᴀᴛᴇғᴏʀᴍ : WhatsApp / Multi-device
┃⌬ ᴅᴇᴠ : {OWNER_NUMBER}
╰━━━━━━━━━━━━━━━◇

╭━━ ◇「 ° {BOT_NAME} ° 」◇
┃⌬ .pair - Connect your device
┃⌬ .delpair - Remove your device
┃⌬ .listpair - View all paired devices
┃⌬ .antidelete - Anti-delete messages
┃⌬ .antilink - Anti-link protection
┃⌬ .promote / .demote / .kickall - Group commands
┃⌬ .image / .video / .song / .tiktok / .yts - Media commands
┃⌬ .bug - Bug / Crash menu (Coming Soon)
┃⌬ .ping - Bot latency
╰━━━━━━━━━━━━━━━◇

Join the channel first to use the bot: {WHATSAPP_CHANNEL}
Contact dev: {TELEGRAM_CONTACT}
"""
    bot.send_message(user, menu)

# Command handlers
def handle_commands(message, user):
    text = message.lower()
    
    # Pair commands
    if text.startswith(".pair") or text.startswith(".delpair") or text.startswith(".listpair"):
        utils.pair_command(bot, message, user, WHATSAPP_CHANNEL)
    
    # Anti-delete
    elif text.startswith(".antidelete"):
        antidelete.run(bot, message, user, WHATSAPP_CHANNEL)
    
    # Anti-link
    elif text.startswith(".antilink"):
        antilink.run(bot, message, user, WHATSAPP_CHANNEL)
    
    # Group commands
    elif text.startswith(".promote") or text.startswith(".demote") or text.startswith(".kickall") or text.startswith(".open") or text.startswith(".close") or text.startswith(".antigroupmention"):
        group_commands.run(bot, message, user)
    
    # Media commands
    elif text.startswith(".image") or text.startswith(".video") or text.startswith(".song") or text.startswith(".tiktok") or text.startswith(".yts") or text.startswith(".vcf"):
        media.run(bot, message, user)
    
    # Bug / Crash commands
    elif text.startswith(".bug"):
        bug_crash.run(bot, message, user)
    
    # Ping
    elif text.startswith(".ping"):
        bot.send_message(user, "🏓 Pong!")

# Main loop
def main():
    for user, message in bot.listen():
        if message.startswith(".start"):
            start_message(user)
        else:
            handle_commands(message, user)

if __name__ == "__main__":
    main()
