// primekillermd/antilink.js
module.exports.run = async (conn, message, sender, channel) => {
    const text = message.message.conversation || message.message.extendedTextMessage?.text;
    if (!text.startsWith('.antilink')) return;

    await conn.sendMessage(sender, '🚫 Antilink is now active!', require('@adiwajshing/baileys').MessageType.text);
    await conn.sendMessage(sender, `Join channel for more: ${channel}`, require('@adiwajshing/baileys').MessageType.text);
    await conn.sendMessage(sender, 'Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧', require('@adiwajshing/baileys').MessageType.text);
};
