// bot.js
const fs = require('fs');
const path = require('path');
const { WAConnection, MessageType, Mimetype } = require('@adiwajshing/baileys');
const primekillermd = require('./primekillermd');

// Load or create pairs.json
const PAIRS_FILE = path.join(__dirname, 'pairs.json');
if (!fs.existsSync(PAIRS_FILE)) fs.writeFileSync(PAIRS_FILE, '{}');
const pairs = JSON.parse(fs.readFileSync(PAIRS_FILE));

const OWNER_NUMBER = '254792770219';
const WHATSAPP_CHANNEL = 'https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l';

async function startBot() {
    const conn = new WAConnection();
    conn.logger.level = 'warn';
    await conn.connect();

    console.log('⛧ＰＲＩＭΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ ɃЦ₲ ɃØŦ is running...');

    conn.on('chat-update', async chatUpdate => {
        if (!chatUpdate.hasNewMessage) return;
        const message = chatUpdate.messages.all()[0];
        if (!message.message) return;
        const sender = message.key.remoteJid;
        const text = message.message.conversation || message.message.extendedTextMessage?.text;
        if (!text) return;

        // Check if user is paired
        const isPaired = pairs[sender];

        // Pairing logic
        if (text.startsWith('.pair ')) {
            const code = text.split(' ')[1];
            if (!code) return conn.sendMessage(sender, 'Enter pairing code: PRIMEMD1', MessageType.text);
            pairs[sender] = code;
            fs.writeFileSync(PAIRS_FILE, JSON.stringify(pairs, null, 2));
            return conn.sendMessage(sender, `✅ Paired successfully with code ${code}`, MessageType.text);
        }

        // Delpair and listpair only for OWNER
        if (sender.includes(OWNER_NUMBER)) {
            if (text.startsWith('.delpair ')) {
                const target = text.split(' ')[1];
                delete pairs[target];
                fs.writeFileSync(PAIRS_FILE, JSON.stringify(pairs, null, 2));
                return conn.sendMessage(sender, `❌ Pair removed for ${target}`, MessageType.text);
            }
            if (text.startsWith('.listpair')) {
                return conn.sendMessage(sender, `📋 Paired devices:\n${JSON.stringify(pairs, null, 2)}`, MessageType.text);
            }
        }

        if (!isPaired) return conn.sendMessage(sender, '❗ You need to pair first using: .pair PRIMEMD1', MessageType.text);

        // Menu command
        if (text.startsWith('.menu')) {
            const menu = `
╭━━ ◇「 PRIME KILLER MD 」◇
┃⌬ BOT: ⛧ＰＲＩΜΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ ɃЦ₲ ɃØŦ
┃⌬ OWNER: ${OWNER_NUMBER}
┃⌬ PLATFORM: WhatsApp
╰━━━━━━━━━━━━━━━◇

╭━━ ◇「 COMMANDS 」◇
┃⌬ .antidelete
┃⌬ .antilink
┃⌬ .promote / .demote / .kickall / .close / .open
┃⌬ .image / .video / .song / .tiktok / .yts
┃⌬ .bug
┃⌬ .ping
╰━━━━━━━━━━━━━━━◇

Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧
Check channel: ${WHATSAPP_CHANNEL}
`;
            return conn.sendMessage(sender, menu, MessageType.text);
        }

        // Handle commands by imported modules
        primekillermd.antidelete.run(conn, message, sender, WHATSAPP_CHANNEL);
        primekillermd.antilink.run(conn, message, sender, WHATSAPP_CHANNEL);
        primekillermd.group_commands.run(conn, message, sender);
        primekillermd.media.run(conn, message, sender);
        primekillermd.bug_crash.run(conn, message, sender);

        // Ping command
        if (text.startsWith('.ping')) {
            conn.sendMessage(sender, '🏓 Pong!', MessageType.text);
        }
    });
}

startBot().catch(err => console.log(err));
