# utils.py
import json
import os

# Pair JSON path
PAIR_FILE = "pairs.json"

# Initialize bot (example placeholder)
def init_bot(owner):
    # Replace with your actual WhatsApp bot initialization
    class Bot:
        def send_message(self, user, msg):
            print(f"[WHATSAPP MESSAGE] To {user}:\n{msg}\n")
        
        def listen(self):
            # Placeholder for listening messages
            while True:
                user = input("User number: ")
                message = input("Message: ")
                yield user, message
    return Bot()

# Return the menu text
def menu_text():
    return """
╭━━ ◇「 ⛧ＰＲＩΜΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ ɃЦ₲ ɃØŦ 」◇
┃⌬ .pair - Connect device
┃⌬ .delpair - Remove device
┃⌬ .listpair - View all devices
┃⌬ .antidelete - Anti Delete
┃⌬ .antilink - Anti Link
┃⌬ .promote - Promote member
┃⌬ .demote - Demote member
┃⌬ .kickall - Kick all
┃⌬ .open - Open group
┃⌬ .close - Close group
┃⌬ .image - Download image
┃⌬ .video - Download video
┃⌬ .song - Download song
┃⌬ .tiktok - Download TikTok
┃⌬ .yts - YouTube search
┃⌬ .vcf - Download VCF
┃⌬ .bug - Bug/Crash
┃⌬ .ping - Bot Ping
╰━━━━━━━━━━━━━━
"""

# Pairing commands
def pair_command(bot, message, user):
    code = "PRIMEMD1"
    number = message.split(" ")[1] if len(message.split(" ")) > 1 else None
    if number:
        # Save paired number
        if os.path.exists(PAIR_FILE):
            with open(PAIR_FILE, "r") as f:
                pairs = json.load(f)
        else:
            pairs = {}

        pairs[number] = {"user": str(user)}
        with open(PAIR_FILE, "w") as f:
            json.dump(pairs, f, indent=4)
        bot.send_message(user, f"✅ Number {number} paired successfully with code {code}")
    else:
        bot.send_message(user, "❌ Please provide your number to pair. Example: .pair 2547xxxxxxx")

# Owner-only commands
def owner_command(bot, message, user):
    text = message.lower()
    if text.startswith(".delpair"):
        number = message.split(" ")[1] if len(message.split(" ")) > 1 else None
        if number and os.path.exists(PAIR_FILE):
            with open(PAIR_FILE, "r") as f:
                pairs = json.load(f)
            if number in pairs:
                pairs.pop(number)
                with open(PAIR_FILE, "w") as f:
                    json.dump(pairs, f, indent=4)
                bot.send_message(user, f"✅ Number {number} removed successfully.")
            else:
                bot.send_message(user, f"❌ Number {number} not found.")
        else:
            bot.send_message(user, "❌ Please provide the number to remove. Example: .delpair 2547xxxxxxx")
    
    elif text.startswith(".listpair"):
        if os.path.exists(PAIR_FILE):
            with open(PAIR_FILE, "r") as f:
                pairs = json.load(f)
            msg = "📃 Paired Numbers:\n"
            for n, data in pairs.items():
                msg += f"{n} -> {data['user']}\n"
            bot.send_message(user, msg)
        else:
            bot.send_message(user, "❌ No paired numbers found.")
