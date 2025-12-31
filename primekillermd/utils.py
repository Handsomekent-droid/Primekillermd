# primekillermd/utils.py
from time import time

# Example bot initializer (replace with your actual WhatsApp bot library)
class WhatsAppBot:
    def __init__(self, owner):
        self.owner = owner
        self.users = {}
    
    def send_message(self, user, message):
        print(f"[Message to {user}]: {message}")
    
    def listen(self):
        """
        Mock listener: yields (user, message) tuples.
        Replace with your WhatsApp library listener.
        """
        while True:
            user_input = input("Message (format user: message): ")
            if ":" in user_input:
                user, msg = user_input.split(":", 1)
                yield user.strip(), msg.strip()

def init_bot(owner):
    """Initialize and return bot instance"""
    return WhatsAppBot(owner)

# Pair command handler
def pair_command(bot, message, user):
    text = message.lower()
    if text.startswith(".pair"):
        bot.send_message(user, "✅ Device paired successfully!")
    elif text.startswith(".delpair"):
        bot.send_message(user, "🗑️ Pair removed successfully!")
    elif text.startswith(".listpair"):
        bot.send_message(user, "📋 List of paired devices:\n1. Device A\n2. Device B")

# Simple ping
def ping(bot, user):
    bot.send_message(user, "🏓 Pong!")

# Uptime function
START_TIME = time()
def runtime(bot, user):
    elapsed = int(time() - START_TIME)
    hours, remainder = divmod(elapsed, 3600)
    minutes, seconds = divmod(remainder, 60)
    bot.send_message(user, f"⏱️ Bot uptime: {hours}h {minutes}m {seconds}s")
