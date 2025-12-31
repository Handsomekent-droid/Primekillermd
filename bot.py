import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# ------------------- BOT CONFIG -------------------
BOT_TOKEN = "8182043616:AAGSfaFaPVx-LM2-ee8-VBaU5MgE2XsifbA"
ADMIN_ID = 8195349331

CHANNEL_LINK = "https://t.me/primekillercrasher"
GROUP_LINK = "https://t.me/primekillercrasherv1"
FUNCTIONS_FOLDER = "primekillermd"

# ------------------- DYNAMIC COMMAND IMPORT -------------------
COMMANDS = {}
for file in os.listdir(FUNCTIONS_FOLDER):
    if file.endswith(".py") and not file.startswith("__"):
        cmd_name = file[:-3]
        module_path = f"{FUNCTIONS_FOLDER}.{cmd_name}"
        try:
            module = __import__(module_path, fromlist=[cmd_name])
            if hasattr(module, "run"):
                COMMANDS[cmd_name] = module.run
        except Exception as e:
            print(f"Failed to import {file}: {e}")

# ------------------- HELPER -------------------
async def check_channel(update: Update) -> bool:
    try:
        member = await update.effective_chat.get_member(update.effective_user.id)
        return True  # Already in chat
    except:
        await update.message.reply_text(
            f"⚠️ You must join our channel first: [Join Here]({CHANNEL_LINK})",
            parse_mode="Markdown"
        )
        return False

# ------------------- COMMAND HANDLERS -------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://i.postimg.cc/L6CPdTdG/file-000000005f2c722f8ccf3dfe281cf45b.png",
        caption=(
            "⛧ＰＲＩＭΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ ɃЦ₲ ɃØŦ\n\n"
            "⚠️ You must join the channel to use the bot:\n"
            f"[Join Channel]({CHANNEL_LINK})\n\n"
            "Type /menu to see all available commands.\n"
            f"Group: [Join Here]({GROUP_LINK})\n\n"
            "Powered by ⛧ＰＲＩＭΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧"
        ),
        parse_mode="Markdown"
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await check_channel(update):
        return
    text = "💀 *Available Commands:*\n\n"
    for cmd in COMMANDS.keys():
        text += f"/{cmd}\n"
    text += "\n/pair <your-number> - Pair WhatsApp"
    text += "\n\nPowered by ⛧ＰＲＩＭΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧"
    await update.message.reply_text(text, parse_mode="Markdown")

async def pair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await check_channel(update):
        return
    if not context.args:
        await update.message.reply_text("Usage: /pair <your-number>")
        return
    number = context.args[0]
    await update.message.reply_text(f"✅ Your WhatsApp number {number} is now paired!\n\nPowered by ⛧ＰＲＩＭΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧")

async def dynamic_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await check_channel(update):
        return
    cmd_name = update.message.text[1:].split()[0]
    if cmd_name in COMMANDS:
        await COMMANDS[cmd_name](update, context)
    else:
        await update.message.reply_text("❌ Command not found.\n\nPowered by ⛧ＰＲＩＭΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧")

# ------------------- BOT APPLICATION -------------------
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Core commands
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("pair", pair))

# Dynamic commands from primekillermd folder
for cmd in COMMANDS.keys():
    app.add_handler(CommandHandler(cmd, COMMANDS[cmd]))

# Catch-all for commands not directly registered
app.add_handler(MessageHandler(filters.Command(), dynamic_command))

# Run bot
print("⛧ＰＲＩＭΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ ɃЦ₲ ɃØŦ is running...")
app.run_polling()
