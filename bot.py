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
⛧ＰＲＩＭΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ ɃЦ₲ ɃØŦ is running...
Owner: {OWNER_NUMBER}
Join the channel first to use the bot: {WHATSAPP_CHANNEL}
"""
    bot.send_message(user, message)

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
    elif text.startswith(".promote") or text.startswith(".demote") or text.startswith(".kickall"):
        group_commands.run(bot, message, user)
    
    # Media commands
    elif text.startswith(".image") or text.startswith(".video") or text.startswith(".song") or text.startswith(".tiktok") or text.startswith(".yts"):
        media.run(bot, message, user)
    
    # Bug crash commands
    elif text.startswith(".bug"):
        bug_crash.run(bot, message, user)
    
    # Pair commands
    elif text.startswith(".pair") or text.startswith(".delpair") or text.startswith(".listpair"):
        utils.pair_command(bot, message, user)

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
