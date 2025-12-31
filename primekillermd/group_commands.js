// primekillermd/group_commands.js
module.exports.run = async (conn, message, sender) => {
    const text = message.message.conversation || message.message.extendedTextMessage?.text;
    const MessageType = require('@adiwajshing/baileys').MessageType;

    if (text.startsWith('.promote')) {
        await conn.sendMessage(sender, '✅ User promoted!', MessageType.text);
    } else if (text.startsWith('.demote')) {
        await conn.sendMessage(sender, '✅ User demoted!', MessageType.text);
    } else if (text.startsWith('.kickall')) {
        await conn.sendMessage(sender, '⚠️ All members kicked (simulated)!', MessageType.text);
    } else if (text.startsWith('.close')) {
        await conn.sendMessage(sender, '🔒 Group is now closed!', MessageType.text);
    } else if (text.startsWith('.open')) {
        await conn.sendMessage(sender, '🔓 Group is now open!', MessageType.text);
    }

    await conn.sendMessage(sender, 'Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧', MessageType.text);
};
