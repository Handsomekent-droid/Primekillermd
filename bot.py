# bot.py
import os
from primekillermd import antidelete, antilink, group_commands, media, bug_crash, utils

# Your channel & contact
WHATSAPP_CHANNEL = "https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l"
OWNER_NUMBER = "254792770219"

# Initialize bot (example using a WhatsApp library)
bot = utils.init_bot(owner=OWNER_NUMBER)

# Welcome message on start
def start_message(user):
    message = f"""
⛧ＰＲＩΜΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ ɃЦ₲ ɃØŦ is running...
Owner: {OWNER_NUMBER}
Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧
"""
    bot.send_message(user, message)

    # Display stylized menu
    menu_text = utils.menu_text()
    bot.send_message(user, menu_text)

    # Prompt for pairing
    bot.send_message(user, "Enter your phone number to pair eg 2547xxxxxxx\nYour pairing code is: PRIMEMD1")

# Command handlers
def handle_commands(message, user):
    text = message.lower()
    
    # Antidelete
    if text.startswith(".antidelete"):
        antidelete.run(bot, message, user, WHATSAPP_CHANNEL)
    
    # Antilink
    elif text.startswith(".antilink"):
        antilink.run(bot, message, user, WHATSAPP_CHANNEL)
    
    # Group commands
    elif text.startswith(".promote") or text.startswith(".demote") or text.startswith(".kickall") or text.startswith(".open") or text.startswith(".close"):
        group_commands.run(bot, message, user)
    
    # Media commands
    elif text.startswith(".image") or text.startswith(".video") or text.startswith(".song") or text.startswith(".tiktok") or text.startswith(".yts") or text.startswith(".vcf"):
        media.run(bot, message, user)
    
    # Bug crash commands
    elif text.startswith(".bug"):
        bug_crash.run(bot, message, user)
    
    # Pair commands
    elif text.startswith(".pair"):
        utils.pair_command(bot, message, user)
    
    # Owner-only commands
    elif text.startswith(".delpair") or text.startswith(".listpair"):
        if str(user) == OWNER_NUMBER:
            utils.owner_command(bot, message, user)
        else:
            bot.send_message(user, "❌ Only the bot owner can use this command.")
    
    # Ping command
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
