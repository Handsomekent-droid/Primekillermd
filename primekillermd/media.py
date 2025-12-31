# bot.py
# Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧
# Channel: https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l

from media import send_image_cmd, send_song_cmd, send_vcf_cmd, send_video_cmd, yts_cmd, tiktok_cmd
from some_whatsapp_library import WhatsAppBot, on_command

bot = WhatsAppBot()

# IMAGE command
@on_command(".image")
def image_handler(chat_id, args):
    if not args:
        bot.send_message(chat_id, "Please provide the image path.")
        return
    send_image_cmd(chat_id, args[0], caption="Here is your image!")

# SONG command
@on_command(".song")
def song_handler(chat_id, args):
    if not args:
        bot.send_message(chat_id, "Please provide the song path.")
        return
    send_song_cmd(chat_id, args[0], title=args[1] if len(args) > 1 else "Your Song")

# VCF command
@on_command(".vcf")
def vcf_handler(chat_id, args):
    if not args:
        bot.send_message(chat_id, "Please provide the VCF file path.")
        return
    send_vcf_cmd(chat_id, args[0])

# VIDEO command
@on_command(".video")
def video_handler(chat_id, args):
    if not args:
        bot.send_message(chat_id, "Please provide the video path.")
        return
    send_video_cmd(chat_id, args[0], caption="Here is your video!")

# YTS command
@on_command(".yts")
def yts_handler(chat_id, args):
    if not args:
        bot.send_message(chat_id, "Please provide a YouTube search query.")
        return
    yts_cmd(chat_id, " ".join(args))

# TIKTOK command
@on_command(".tiktok")
def tiktok_handler(chat_id, args):
    if not args:
        bot.send_message(chat_id, "Please provide a TikTok URL.")
        return
    tiktok_cmd(chat_id, args[0])

# Start the bot
bot.start()
