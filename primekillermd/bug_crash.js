// primekillermd/bug_crash.js
module.exports.run = async (conn, message, sender) => {
    const text = message.message.conversation || message.message.extendedTextMessage?.text;
    const MessageType = require('@adiwajshing/baileys').MessageType;

    if (!text.startsWith('.bug')) return;

    await conn.sendMessage(sender, '💥 Bug/Crash functions coming soon!', MessageType.text);
    await conn.sendMessage(sender, 'Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧', MessageType.text);
};
