const { default: makeWASocket, DisconnectReason } = require("@adiwajshing/baileys");
const P = require('pino');
const fs = require('fs');

const PAIRING_CODE = "PRIMEMD1";
const TELEGRAM_CHANNEL = "https://t.me/primekillercrasher";
const SUPPORT_LINK = "https://t.me/Handsome_primis_killer_kent";
const MENU_IMAGE_URL = "https://i.postimg.cc/8csPm0dz/file-000000005f2c722f8ccf3dfe281cf45b.png";

// Load or create paired users JSON
let pairs = {};
try {
    pairs = JSON.parse(fs.readFileSync("pairs.json"));
} catch {
    pairs = {};
}

// ---------------- START BOT ----------------
async function startBot() {
    const sock = makeWASocket({ logger: P({ level: 'silent' }), printQRInTerminal: true });

    sock.ev.on('messages.upsert', async m => {
        const msg = m.messages[0];
        if (!msg.message) return;
        const from = msg.key.remoteJid;
        const text = msg.message.conversation;

        // ---------------- PAIRING ----------------
        if (text === PAIRING_CODE) {
            pairs[from] = true;
            fs.writeFileSync("pairs.json", JSON.stringify(pairs, null, 2));

            await sock.sendMessage(from, {
                image: { url: MENU_IMAGE_URL },
                caption: `✅ Paired successfully!\nType .menu to see commands.\nChannel: ${TELEGRAM_CHANNEL}`
            });
        }

        // ---------------- MENU ----------------
        if (text === ".menu") {
            if (!pairs[from]) {
                await sock.sendMessage(from, { text: "❌ You are not paired. Type PRIMEMD1 to connect first." });
                return;
            }

            const menuText = `
╭━━━━━━━━━━━━━━━━━━━━━━━╮
│ ☠️👁️🩸 P҉r҉i҉m҉e҉ ✞ K҉i҉l҉l҉e҉r҉ ✞ C҉r҉a҉s҉h҉e҉r҉ B҉o҉t 🩸👁️☠️
│
│ ⚠️ Mode       : public
│ 💀 User       : ${from.split("@")[0]}
│ 🕷️ Platform   : WhatsApp
│ 🩸 Dev        : P҉r҉i҉m҉e҉ ✞ kîllér ✞ K҉e҉n҉t
│ ☠️ Version    : 1.0.0
╰━━━━━━━━━━━━━━━━━━━━━━━╯

╭━━━━━━〘 ⚔️ ᴳᴿᴼᵁᴾ ᴹᴱᴺᵁ ⚔️ 〙━━━━━━╮
│ 🩸 .promote           ─ Promote member to admin
│ 🩸 .demote            ─ Remove admin from member
│ 🩸 .kick              ─ Remove member
│ 🩸 .kickall           ─ Remove all members
│ 🩸 .tagall            ─ Mention all members
│ 🩸 .tagadmin          ─ Mention all admins
│ 🩸 .antilink          ─ Block group links
│ 🩸 .antidelete        ─ Prevent message deletion
│ 🩸 .antigroupmention  ─ Prevent mass mentions
╰━━━━━━━━━━━━━━━━━━━━━━━━╯

╭━━━━━━〘 🎵 ᴹᴱᴰᴵᴬ ᴹᴱᴺᵁ 🎵 〙━━━━━━╮
│ 🕸️ .song          ─ Download any song
│ 🕸️ .video         ─ Download any video
│ 🕸️ .play          ─ Play song or video
│ 🕸️ .tiktok        ─ Download TikTok video
│ 🕸️ .youtube       ─ Download YouTube video
│ 🕸️ .filter         ─ Apply media filters
╰━━━━━━━━━━━━━━━━━━━━━━━━╯

╭━━━━━━〘 📋 ᴸᴵˢᵀˢ ᴹᴱᴺᵁ 📋 〙━━━━━━╮
│ 🔪 .listonline    ─ Show online users
│ 🔪 .listactive    ─ Show active users
│ 🔪 .listinactive  ─ Show inactive users
│ 🔪 .listadmins     ─ Show group admins
│ 🔪 .listgroups     ─ Show joined groups
╰━━━━━━━━━━━━━━━━━━━━━━━━╯

╭━━━━━━〘 ⚡ ᴱˣᵀᴿᴬ ᴹᴱᴺᵁ ⚡ 〙━━━━━━╮
│ 💀 .info           ─ Bot information
│ 💀 .status         ─ Bot current status
│ 💀 .help           ─ Show all commands
│ 💀 .support        ─ Contact support
│ 💀 .ping           ─ Bot latency test
╰━━━━━━━━━━━━━━━━━━━━━━━━╯

☠️🩸 Telegram Channel: ${TELEGRAM_CHANNEL} 🩸☠️
💬 Contact Support: ${SUPPORT_LINK}
`;

            await sock.sendMessage(from, {
                image: { url: MENU_IMAGE_URL },
                caption: menuText
            });
        }

        // ---------------- SUPPORT ----------------
        if (text === ".support") {
            await sock.sendMessage(from, {
                image: { url: MENU_IMAGE_URL },
                caption: `💬 Contact Support:\nReach out to the developer on Telegram:\n${SUPPORT_LINK}`
            });
        }

        // ---------------- PING ----------------
        if (text === ".ping") {
            const start = Date.now();
            await sock.sendMessage(from, { image: { url: MENU_IMAGE_URL }, caption: "🏓 Pinging..." });
            const end = Date.now();
            await sock.sendMessage(from, { image: { url: MENU_IMAGE_URL }, caption: `🏓 Pong! Latency: ${end - start}ms` });
        }

        // ---------------- MEDIA COMMAND PLACEHOLDER ----------------
        if (text.startsWith(".song") || text.startsWith(".video") || text.startsWith(".play") ||
            text.startsWith(".tiktok") || text.startsWith(".youtube")) {

            await sock.sendMessage(from, {
                image: { url: MENU_IMAGE_URL },
                caption: `🎵 Your request is being processed!\nChannel: ${TELEGRAM_CHANNEL}`
            });

            // Add your media processing logic here
        }
    });

    // ---------------- CONNECTION UPDATE ----------------
    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect } = update;
        if (connection === 'close') {
            if ((lastDisconnect?.error)?.output?.statusCode !== DisconnectReason.loggedOut) {
                startBot(); // Reconnect if not logged out
            }
        }
        console.log('Connection update:', update);
    });

    console.log("✅ WhatsApp bot is running...");
}

startBot();
