# primekillermd/antilink.py

"""
Antilink command module for Prime Killer MD Bot
Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧
"""

from some_whatsapp_library import send_message  # Replace with your WhatsApp library import

CHANNEL_LINK = "https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l"

async def antilink(chat_id, message_text, sender_name=None):
    """
    Detects links in chat messages and deletes or warns the sender.
    
    Args:
        chat_id: ID of the chat where the message was sent
        message_text: The content of the message
        sender_name: Optional, name of the sender
    """
    import re
    # Simple regex to detect URLs
    url_pattern = r"(https?://\S+)"
    if re.search(url_pattern, message_text):
        user_text = f" from {sender_name}" if sender_name else ""
        notification_text = (
            f"🚫 Link detected{user_text}!\n"
            f"Links are not allowed in this group.\n"
            f"Check our official channel for updates: {CHANNEL_LINK}"
        )
        await send_message(chat_id, notification_text)
        # Optionally, delete the message using your WhatsApp library
        # await delete_message(chat_id, message_id)
