# primekillermd/group_commands.py

"""
Group Commands Module for Prime Killer MD Bot
Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧
"""

from some_whatsapp_library import (
    promote_member,
    demote_member,
    remove_member,
    add_member,
    mention_all,
    send_message,
    set_group_name,
    set_group_desc,
    set_group_rules,
    set_group_profile_pic,
    close_group,
    open_group,
    kick_all_members
)  # Replace with your WhatsApp library functions

CHANNEL_LINK = "https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l"

# --- Admin / Owner Commands ---

async def promote(chat_id, user_id):
    await promote_member(chat_id, user_id)
    await send_message(chat_id, f"✅ User {user_id} has been promoted!\nChannel: {CHANNEL_LINK}\nPowered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧")

async def demote(chat_id, user_id):
    await demote_member(chat_id, user_id)
    await send_message(chat_id, f"⚠️ User {user_id} has been demoted!\nChannel: {CHANNEL_LINK}\nPowered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧")

async def remove(chat_id, user_id):
    await remove_member(chat_id, user_id)
    await send_message(chat_id, f"❌ User {user_id} has been removed from the group.\nChannel: {CHANNEL_LINK}")

async def add(chat_id, user_id):
    await add_member(chat_id, user_id)
    await send_message(chat_id, f"➕ User {user_id} has been added to the group.\nChannel: {CHANNEL_LINK}")

async def mention_all_members(chat_id):
    await mention_all(chat_id)
    await send_message(chat_id, f"📢 All members have been mentioned!\nChannel: {CHANNEL_LINK}")

async def set_group_name_cmd(chat_id, new_name):
    await set_group_name(chat_id, new_name)
    await send_message(chat_id, f"✏️ Group name changed to '{new_name}'\nChannel: {CHANNEL_LINK}")

async def set_group_desc_cmd(chat_id, description):
    await set_group_desc(chat_id, description)
    await send_message(chat_id, f"📝 Group description updated.\nChannel: {CHANNEL_LINK}")

async def set_group_rules_cmd(chat_id, rules):
    await set_group_rules(chat_id, rules)
    await send_message(chat_id, f"📜 Group rules updated.\nChannel: {CHANNEL_LINK}")

async def set_group_profile_pic_cmd(chat_id, image_path):
    await set_group_profile_pic(chat_id, image_path)
    await send_message(chat_id, f"🖼️ Group profile picture updated.\nChannel: {CHANNEL_LINK}")

# --- Protection Commands ---

async def antidelete(chat_id):
    await send_message(chat_id, f"🚫 Message deletion is blocked!\nChannel: {CHANNEL_LINK}")

async def antilink(chat_id):
    await send_message(chat_id, f"🔗 Sending links is not allowed!\nChannel: {CHANNEL_LINK}")

async def antigroupmention(chat_id):
    await send_message(chat_id, f"🚫 Mass mentions are not allowed!\nChannel: {CHANNEL_LINK}")

# --- Group Control Commands ---

async def close_group_cmd(chat_id):
    await close_group(chat_id)
    await send_message(chat_id, f"🔒 Group has been closed (only admins can send messages).\nChannel: {CHANNEL_LINK}")

async def open_group_cmd(chat_id):
    await open_group(chat_id)
    await send_message(chat_id, f"🔓 Group is now open for all members to chat.\nChannel: {CHANNEL_LINK}")

async def kick_all_cmd(chat_id):
    await kick_all_members(chat_id)
    await send_message(chat_id, f"⚠️ All non-admin members have been removed!\nChannel: {CHANNEL_LINK}")

# --- Owner Only Command ---

async def owner_only(chat_id, command_name):
    await send_message(chat_id, f"⚠️ The command '{command_name}' can only be used by the owner.\nChannel: {CHANNEL_LINK}")
