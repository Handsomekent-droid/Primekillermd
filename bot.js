// bot.js
const fs = require('fs');
const path = require('path');
const { Client } = require('whatsapp-web.js'); // Example library
const qrcode = require('qrcode-terminal');

const utils = require('./primekillermd/utils');
const antidelete = require('./primekillermd/antidelete');
const antilink = require('./primekillermd/antilink');
const groupCommands = require('./primekillermd/group_commands');
const media = require('./primekillermd/media');
const bugCrash = require('./primekillermd/bug_crash');

const PAIRS_FILE = path.join(__dirname, 'pairs.json');
const ADMIN_NUMBER = "254792770219"; // Your number
const WHATSAPP_CHANNEL = "https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l";

let pairs = {};
if (fs.existsSync(PAIRS_FILE)) {
    pairs = JSON.parse(fs.readFileSync(PAIRS_FILE));
}

// Initialize WhatsApp client
const client = new Client();

client.on('qr', qr => {
    qrcode.generate(qr, { small: true });
    console.log("Scan QR to connect WhatsApp.");
});

client.on('ready', () => {
    console.log("⛧ＰＲＩＭΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ ɃЦ₲ ɃØŦ is online!");
});

// Listen to messages
client.on('message', async msg => {
    const senderNumber = msg.from.replace(/[^0-9]/g, '');
    const text = msg.body.trim();

    // Log to panel console
    console.log("==================================================");
    console.log("[WHATSAPP MESSAGE]");
    console.log(`From : ${senderNumber}`);
    console.log(`Text : ${text}`);
    console.log("==================================================");

    // Handle pairing
    if (text.startsWith('.pair ')) {
        const number = text.split(' ')[1];
        if (!pairs[number]) {
            pairs[number] = { pairedAt: new Date().toISOString() };
            fs.writeFileSync(PAIRS_FILE, JSON.stringify(pairs, null, 2));
            client.sendMessage(msg.from, `✅ Paired successfully! You can now use the bot on WhatsApp.`);
        } else {
            client.sendMessage(msg.from, "⚠️ This number is already paired.");
        }
        return;
    }

    if (!pairs[senderNumber] && senderNumber !== ADMIN_NUMBER) {
        client.sendMessage(msg.from, "Enter your phone number to pair e.g., 2547xxxxxxx. Your pairing code is PRIMEMD1");
        return;
    }

    // Admin commands
    if (senderNumber === ADMIN_NUMBER) {
        if (text.startsWith('.delpair ')) {
            const number = text.split(' ')[1];
            if (pairs[number]) {
                delete pairs[number];
                fs.writeFileSync(PAIRS_FILE, JSON.stringify(pairs, null, 2));
                client.sendMessage(msg.from, `🗑️ Pair ${number} deleted successfully.`);
            } else {
                client.sendMessage(msg.from, "⚠️ Number not found in pairs.");
            }
            return;
        }
        if (text === '.listpair') {
            let list = Object.keys(pairs).map(n => `• ${n}`).join('\n') || 'No paired numbers';
            client.sendMessage(msg.from, `📋 Paired Numbers:\n${list}`);
            return;
        }
    }

    // General commands
    if (text.startsWith('.antidelete')) return antidelete.run(client, msg, WHATSAPP_CHANNEL);
    if (text.startsWith('.antilink')) return antilink.run(client, msg, WHATSAPP_CHANNEL);
    if (text.startsWith('.promote') || text.startsWith('.demote') || text.startsWith('.kickall')) return groupCommands.run(client, msg);
    if (text.startsWith('.image') || text.startsWith('.video') || text.startsWith('.song') || text.startsWith('.tiktok') || text.startsWith('.yts')) return media.run(client, msg);
    if (text.startsWith('.bug')) return bugCrash.run(client, msg);

    // Ping command
    if (text === '.ping') {
        client.sendMessage(msg.from, '🏓 Pong!');
    }

    // Menu command
    if (text === '.menu') {
        const menuMessage = `
╭━━ ◇「 ⛧ＰＲＩＭΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ ɃЦ₲ ɃØŦ 」◇
┃⌬ Owner : ${ADMIN_NUMBER}
┃⌬ Platform : WhatsApp
┃⌬ Powered by : ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧
╰━━━━━━━━━━━━━━
Bug Crash: Coming Soon
Media Commands: .image, .video, .song, .tiktok, .yts
Group Commands: .promote, .demote, .kickall
Utility: .antidelete, .antilink, .ping
Pair Commands: .pair, .delpair (admin only), .listpair (admin only)

View channel: ${WHATSAPP_CHANNEL}
`;
        client.sendMessage(msg.from, menuMessage);
    }
});

client.initialize();
