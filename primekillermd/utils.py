import json
import os

PAIRS_FILE = "pairs.json"

def load_pairs():
    if not os.path.exists(PAIRS_FILE):
        with open(PAIRS_FILE, "w") as f:
            json.dump({"paired_users": []}, f)
    with open(PAIRS_FILE, "r") as f:
        return json.load(f)

def save_pairs(data):
    with open(PAIRS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def pair_command(bot, message, user):
    data = load_pairs()
    text = message.lower()

    # Pair new user
    if text.startswith(".pair"):
        if user not in data["paired_users"]:
            data["paired_users"].append(user)
            save_pairs(data)
            bot.send_message(user, f"✅ {user} paired successfully!\nJoin the channel first: https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l")
        else:
            bot.send_message(user, "⚠️ Already paired!")

    # Delete user pair
    elif text.startswith(".delpair"):
        if user in data["paired_users"]:
            data["paired_users"].remove(user)
            save_pairs(data)
            bot.send_message(user, "❌ Pair removed successfully!")
        else:
            bot.send_message(user, "⚠️ You are not paired!")

    # List paired users (admin only)
    elif text.startswith(".listpair"):
        paired = "\n".join(data["paired_users"]) if data["paired_users"] else "No users paired yet."
        bot.send_message(user, f"📋 Paired users:\n{paired}")
