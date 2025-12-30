from telegram import Update, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ---------------- CONFIG ----------------
TOKEN = '8182043616:AAGSfaFaPVx-LM2-ee8-VBaU5MgE2XsifbA'  # Your Telegram bot token
ADMIN_ID = 8195349331                                     # Your Telegram ID
TELEGRAM_CHANNEL = "https://t.me/primekillercrasher"
MENU_IMAGE_URL = "https://i.postimg.cc/8csPm0dz/file-000000005f2c722f8ccf3dfe281cf45b.png"
# ----------------------------------------

paired_users = {}

# ---------------- COMMANDS ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"👋 Hello {update.effective_user.first_name}!\n"
        "🤖 Telegram Bot is online!\n"
        "🔗 Connect to WhatsApp with /connect <number>\n"
        "📜 View menu: /menu"
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu_text = f"""
╭━━━━━━━━━━━━━━━╮
│あ  🤖  ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ɪɴғᴏ
╰━━━━━━━━━━━━━━━╯
│あ  ✦ ɴᴀᴍᴇ    : P҉r҉i҉m҉e҉ ✞ K҉i҉l҉l҉e҉r҉ ✞ C҉r҉a҉s҉h҉e҉r҉ B҉o҉t
│あ  ✦ ᴅᴇᴠ     : P҉r҉i҉m҉e҉ ✞ kîllér ✞ K҉e҉n҉t҉
│あ  ✦ ᴠᴇʀsɪᴏɴ : 1.0.0
│あ  ✦ sᴛᴀᴛᴜs  : ᴏɴʟɪɴᴇ ✅
│あ  ✦ ᴘʟᴀᴛғᴏʀᴍ: ᴛᴇʟᴇɢʀᴀᴍ
│あ  ✦ ᴘʀᴇғɪx  : /
╰━━━━━━━━━━━━━━━╯

╭━━━━〘 ⚔ ᴄᴏᴍᴍᴀɴᴅs ⚔ 〙━━━━╮
│あ   ✧ /start       ─ Start the bot
│あ   ✧ /menu        ─ Show this menu
│あ   ✧ /connect     ─ Link to WhatsApp account
│あ   ✧ /listpair    ─ Show linked users (Admin Only)
╰━━━━━━━━━━━━━━━━━━━━━━━━╯

🔗 Channel: {TELEGRAM_CHANNEL}
"""
    # Send the image with caption
    await update.message.reply_photo(photo=MENU_IMAGE_URL, caption=menu_text)

async def connect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if len(context.args) == 0:
        await update.message.reply_text("❌ Usage: /connect <number>")
        return
    number = context.args[0]
    paired_users[user_id] = number
    await update.message.reply_text(
        f"✅ Paired {number} successfully!\n"
        "Use code PRIMEMD1 on WhatsApp to complete linking."
    )

async def listpair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text("❌ You are not allowed to use this command.")
        return
    if not paired_users:
        await update.message.reply_text("No users paired yet.")
        return
    text = "📋 Paired Users:\n"
    for user, number in paired_users.items():
        text += f"- {number}\n"
    await update.message.reply_text(text)

# ---------------- SETUP BOT ----------------
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("connect", connect))
app.add_handler(CommandHandler("listpair", listpair))

print("✅ P҉r҉i҉m҉e҉ ✞ K҉i҉l҉l҉e҉r҉ ✞ C҉r҉a҉s҉h҉e҉r҉ ✞ B҉o҉t҉ is running...")
app.run_polling()
