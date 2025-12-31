# primekillermd/antidelete.py

"""
Antidelete command module for Prime Killer MD Bot
Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧
"""

from some_whatsapp_library import send_message  # Replace with your WhatsApp library import

CHANNEL_LINK = "https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l"

async def antidelete(chat_id, message_id, user_name=None):
    """
    Detects deleted messages and notifies the chat.
    
    Args:
        chat_id: ID of the chat where the message was deleted
        message_id: ID of the deleted message
        user_name: Optional, name of the user who deleted the message
    """
    user_text = f" by {user_name}" if user_name else ""
    notification_text = (
        f"🛡️ A message was deleted{user_text}!\n"
        f"Can't hide from Prime Killer MD Bot!\n"
        f"View our official channel for updates: {CHANNEL_LINK}"
    )

    await send_message(chat_id, notification_text)
