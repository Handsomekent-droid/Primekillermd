// primekillermd/media.js
module.exports.run = async (conn, message, sender) => {
    const text = message.message.conversation || message.message.extendedTextMessage?.text;
    const MessageType = require('@adiwajshing/baileys').MessageType;

    if (text.startsWith('.image')) {
        await conn.sendMessage(sender, '🖼️ Sending image...', MessageType.text);
    } else if (text.startsWith('.video')) {
        await conn.sendMessage(sender, '🎥 Sending video...', MessageType.text);
    } else if (text.startsWith('.song')) {
        await conn.sendMessage(sender, '🎵 Sending song...', MessageType.text);
    } else if (text.startsWith('.tiktok')) {
        await conn.sendMessage(sender, '📱 Sending TikTok video...', MessageType.text);
    } else if (text.startsWith('.yts')) {
        await conn.sendMessage(sender, '🔍 Searching YouTube...', MessageType.text);
    }

    await conn.sendMessage(sender, 'Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧', MessageType.text);
};
