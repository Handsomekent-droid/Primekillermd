# utils.py
# Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧
# Channel: https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l

from some_whatsapp_library import WhatsAppBot

bot = WhatsAppBot()

# Send a formatted message
def send_message(chat_id, text, link_channel=True):
    """
    Send a message to the user.
    Optionally adds 'View Channel' at the bottom.
    """
    if link_channel:
        text += "\n\nView Channel: https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l"
    bot.send_message(chat_id, text)

# Check if user is the owner
def is_owner(user_id):
    """
    Replace 'YOUR_NUMBER' with your WhatsApp number.
    Returns True if user is the bot owner.
    """
    return str(user_id) == "254792770219"

# Format command menu
def format_menu(bot_name="Prime Killer MD", user_name="", platform="WhatsApp"):
    """
    Returns a decorated string for the bot menu
    """
    menu_text = f"""
╭━━ ◇「 ° INFOBOT ° 」◇
┃⌬ ʙᴏᴛ : {bot_name}
┃⌬ ᴜsᴇʀ : {user_name}
┃⌬ ᴘʟᴀᴛᴇғᴏʀᴍ : {platform}
┃⌬ ᴅᴇᴠ : ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧
╰━━━━━━━━━━━━━━━◇
"""
    return menu_text

# Helper to join arguments into a string
def args_to_text(args):
    return " ".join(args) if args else ""

# Example function to safely get a file path
def validate_file(file_path):
    import os
    return file_path if os.path.exists(file_path) else None

# Utility for error messages
def send_error(chat_id, error_msg):
    bot.send_message(chat_id, f"❌ Error: {error_msg}")
