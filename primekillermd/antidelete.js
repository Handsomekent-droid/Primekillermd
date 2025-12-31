// primekillermd/antidelete.js
module.exports.run = async (conn, message, sender, channel) => {
    const text = message.message.conversation || message.message.extendedTextMessage?.text;
    if (!text.startsWith('.antidelete')) return;

    // Example functionality: confirm antidelete is ON
    await conn.sendMessage(sender, '🛡️ Antidelete is now active!', require('@adiwajshing/baileys').MessageType.text);
    await conn.sendMessage(sender, `Check updates & channel: ${channel}`, require('@adiwajshing/baileys').MessageType.text);

    // Powered by you
    await conn.sendMessage(sender, 'Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧', require('@adiwajshing/baileys').MessageType.text);
};
