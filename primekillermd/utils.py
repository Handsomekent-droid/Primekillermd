# primekillermd/utils.py

import json
import os
import time

# =========================
# CONFIG
# =========================
OWNER_NUMBER = "254792770219"
PAIR_CODE = "PRIMEMD1"
PAIRS_FILE = "pairs.json"


# =========================
# JSON PAIR STORAGE
# =========================
def load_pairs():
    if not os.path.exists(PAIRS_FILE):
        with open(PAIRS_FILE, "w") as f:
            json.dump([], f)
    with open(PAIRS_FILE, "r") as f:
        return json.load(f)


def save_pairs(data):
    with open(PAIRS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def is_paired(number):
    pairs = load_pairs()
    return number in pairs


# =========================
# PANEL LOGGING
# =========================
def log_whatsapp_message(sender, chat, text):
    print("=" * 50)
    print("[WHATSAPP MESSAGE]")
    print(f"From : {sender}")
    print(f"Chat : {chat}")
    print(f"Text : {text}")
    print("=" * 50)


def log_status(text):
    print("=" * 50)
    print("[BOT STATUS]")
    print(text)
    print("=" * 50)


# =========================
# PAIRING COMMANDS
# =========================
def pair_command(message):
    sender = message.sender
    text = message.text.strip()

    pairs = load_pairs()

    # Already paired
    if sender in pairs:
        message.reply("✅ Your number is already paired.")
        return

    # Pair code check
    if text != f".pair {PAIR_CODE}":
        message.reply(
            "❌ Invalid pair code.\n\n"
            "Enter your phone number to pair  eg 2547xxxxxxx\n"
            "Then use:\n"
            f".pair {PAIR_CODE}"
        )
        return

    # Save pairing
    pairs.append(sender)
    save_pairs(pairs)

    message.reply(
        "✅ PAIR SUCCESSFUL!\n\n"
        "You can now use all bot commands on WhatsApp.\n\n"
        "Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧"
    )

    log_status(f"New device paired: {sender}")


def delpair_command(message):
    sender = message.sender
    text = message.text.strip()

    if sender != OWNER_NUMBER:
        message.reply("❌ Owner only command.")
        return

    parts = text.split()
    if len(parts) != 2:
        message.reply("Usage: .delpair 2547xxxxxxx")
        return

    target = parts[1]
    pairs = load_pairs()

    if target not in pairs:
        message.reply("❌ Number not paired.")
        return

    pairs.remove(target)
    save_pairs(pairs)

    message.reply(f"✅ Removed pairing for {target}")
    log_status(f"Pair removed: {target}")


def listpair_command(message):
    sender = message.sender

    if sender != OWNER_NUMBER:
        message.reply("❌ Owner only command.")
        return

    pairs = load_pairs()

    if not pairs:
        message.reply("No paired devices.")
        return

    text = "📱 *PAIRED DEVICES*\n\n"
    for num in pairs:
        text += f"• {num}\n"

    message.reply(text)


# =========================
# ACCESS CONTROL
# =========================
def check_access(message):
    sender = message.sender

    if sender == OWNER_NUMBER:
        return True

    if not is_paired(sender):
        message.reply(
            "❌ Device not paired.\n\n"
            "Enter your phone number to pair  eg 2547xxxxxxx\n"
            f"Then use:\n.pair {PAIR_CODE}"
        )
        return False

    return True


# =========================
# PING
# =========================
def ping(message):
    start = time.time()
    end = time.time()
    message.reply(f"🏓 Pong!\nSpeed: {round((end - start)*1000)}ms")
