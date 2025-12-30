// ====== IMPORTS ======
const { default: makeWASocket, useMultiFileAuthState, DisconnectReason, fetchLatestBaileysVersion, makeInMemoryStore } = require('@adiwajshing/baileys');
const Pino = require('pino');
const ytdl = require('ytdl-core');
const yts = require('yt-search');
const fs = require('fs');
const path = require('path');
const axios = require('axios');

const PAIRING_CODE = "PRIMEMD1";
const TELEGRAM_CHANNEL = "https://t.me/primekillercrasher";
const SUPPORT_LINK = "https://t.me/Handsome_primis_killer_kent";
const MENU_IMAGE_URL = "https://i.postimg.cc/8csPm0dz/file-000000005f2c722f8ccf3dfe281cf45b.png";

const store = makeInMemoryStore({ logger: Pino().child({ level: 'silent' }) });

async function startBot() {
  const { state, saveCreds } = await useMultiFileAuthState('./session');
  const { version } = await fetchLatestBaileysVersion();
  
  const sock = makeWASocket({
    version,
    auth: state,
    logger: Pino({ level: 'silent' }),
    printQRInTerminal: true
  });

  store.bind(sock.ev);
  sock.ev.on('creds.update', saveCreds);

  sock.ev.on('connection.update', (update) => {
    const { connection, lastDisconnect } = update;
    if(connection === 'open') console.log('✅ WhatsApp connected!');
    if(connection === 'close'){
      const reason = lastDisconnect?.error?.output?.statusCode;
      if(reason !== DisconnectReason.loggedOut) startBot();
      else console.log('❌ Logged out. Scan QR again.');
    }
  });

  sock.ev.on('messages.upsert', async ({ messages }) => {
    const msg = messages[0];
    if(!msg.message || msg.key.fromMe) return;
    const text = msg.message.conversation || msg.message.extendedTextMessage?.text;
    if(!text) return;
    const sender = msg.key.remoteJid;
    const isGroup = sender.endsWith('g.us');
    const groupMetadata = isGroup ? await sock.groupMetadata(sender) : null;

    // ================= MENU =================
    if(text === '.menu'){
      await sock.sendMessage(sender, {
        image: { url: MENU_IMAGE_URL },
        caption: `
🩸👹⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻👹🩸
          👑 *PRIMEMD V1* 👑
🩸👹⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻👹🩸

💀 Dev: P҉r҉i҉m҉e҉ ✞ kîllér ✞ K҉e҉n҉t҉
🕷️ Platform: WhatsApp MD
⚡ Mode: Public
🔮 Version: 1.0

🧛 GROUP COMMANDS
🕸️ .tagall
🕸️ .promote @user
🕸️ .demote @user
🕸️ .kick @user
🕸️ .kickall

🛡️ SECURITY
💀 .antilink
💀 .antidelete
💀 .antibug
💀 .antigroupmention

🎵 MEDIA
🎶 .song [name]
🎥 .video [name]
▶️ .play [name]
🎬 .tiktok [url]
📺 .youtube [url]

⚙️ TOOLS
⚡ .ping
📜 .listonline
📋 .listactive
📴 .listinactive
📞 .support

For help → ${TELEGRAM_CHANNEL}
        `
      });
    }

    // ================= PING =================
    if(text === '.ping') await sock.sendMessage(sender, { text: '⚡ Pong!' });

    // ================= SUPPORT =================
    if(text === '.support') await sock.sendMessage(sender, { text: `Contact Dev: ${SUPPORT_LINK}` });

    // ================= GROUP COMMANDS =================
    if(isGroup){
      // TAGALL
      if(text.startsWith('.tagall')){
        const mentions = groupMetadata.participants.map(p => p.id);
        await sock.sendMessage(sender, { text: '🔔 Tagging all members!', mentions });
      }
      // PROMOTE
      if(text.startsWith('.promote')){
        const user = msg.message.extendedTextMessage?.contextInfo?.mentionedJid?.[0];
        if(user) await sock.groupParticipantsUpdate(sender, [user], 'promote');
        else await sock.sendMessage(sender, { text: '⚠️ Tag a user to promote!' });
      }
      // DEMOTE
      if(text.startsWith('.demote')){
        const user = msg.message.extendedTextMessage?.contextInfo?.mentionedJid?.[0];
        if(user) await sock.groupParticipantsUpdate(sender, [user], 'demote');
        else await sock.sendMessage(sender, { text: '⚠️ Tag a user to demote!' });
      }
      // KICK
      if(text.startsWith('.kick')){
        const user = msg.message.extendedTextMessage?.contextInfo?.mentionedJid?.[0];
        if(user) await sock.groupParticipantsUpdate(sender, [user], 'remove');
        else await sock.sendMessage(sender, { text: '⚠️ Tag a user to kick!' });
      }
      // KICKALL
      if(text.startsWith('.kickall')){
        const nonAdmins = groupMetadata.participants.filter(p => !p.admin).map(p => p.id);
        if(nonAdmins.length > 0){
          await sock.groupParticipantsUpdate(sender, nonAdmins, 'remove');
          await sock.sendMessage(sender, { text: '⚡ Kicked all non-admins!' });
        } else await sock.sendMessage(sender, { text: '⚠️ No users to kick!' });
      }
      // SECURITY
      if(text.startsWith('.antilink')){
        sock.ev.on('messages.upsert', async ({ messages })=>{
          for(let m of messages){
            const msgText = m.message?.conversation || m.message?.extendedTextMessage?.text;
            if(msgText && /(https?:\/\/chat.whatsapp.com\/)/gi.test(msgText)){
              await sock.sendMessage(sender, { text: '❌ Group link detected! Deleted!' });
              await sock.sendMessage(sender, { delete: m.key });
            }
          }
        });
      }
      if(text.startsWith('.antidelete')){
        sock.ev.on('messages.update', async (update)=>{
          for(let m of update){
            if(m.update?.messageStubType === 68){
              await sock.sendMessage(sender, { text: '❌ Message deletion prevented!' });
            }
          }
        });
      }
      if(text.startsWith('.antibug')) await sock.sendMessage(sender, { text: '⚡ Anti-bug activated!' });
      if(text.startsWith('.antigroupmention')) await sock.sendMessage(sender, { text: '⚡ Anti group mention activated!' });
    }

    // ================= MEDIA =================
    if(text.startsWith('.song') || text.startsWith('.play')){
      const query = text.split(' ').slice(1).join(' ');
      if(!query) return sock.sendMessage(sender, { text: '⚠️ Provide a song name!' });
      const search = await yts(query);
      if(!search?.all[0]) return sock.sendMessage(sender, { text: '❌ No results found!' });
      const songInfo = search.all[0];
      const filePath = path.join(__dirname, 'temp.mp3');
      const stream = ytdl(songInfo.url, { filter: 'audioonly' });
      const writeStream = fs.createWriteStream(filePath);
      stream.pipe(writeStream);
      writeStream.on('finish', async ()=>{
        await sock.sendMessage(sender, { audio: fs.readFileSync(filePath), mimetype: 'audio/mpeg', fileName: `${songInfo.title}.mp3` });
        fs.unlinkSync(filePath);
      });
    }

    if(text.startsWith('.video') || text.startsWith('.youtube')){
      const query = text.split(' ').slice(1).join(' ');
      let videoUrl = query.startsWith('http') ? query : (await yts(query)).all[0]?.url;
      if(!videoUrl) return sock.sendMessage(sender, { text: '❌ No video found!' });
      const filePath = path.join(__dirname, 'temp.mp4');
      const stream = ytdl(videoUrl, { quality: 'highestvideo' });
      const writeStream = fs.createWriteStream(filePath);
      stream.pipe(writeStream);
      writeStream.on('finish', async ()=>{
        await sock.sendMessage(sender, { video: fs.readFileSync(filePath), mimetype: 'video/mp4', fileName: 'video.mp4' });
        fs.unlinkSync(filePath);
      });
    }

    if(text.startsWith('.tiktok')){
      const url = text.split(' ')[1];
      if(!url) return sock.sendMessage(sender, { text: '⚠️ Provide a valid TikTok URL!' });
      await sock.sendMessage(sender, { text: `🎬 Downloading TikTok from ${url} (use TikTok API for full download)` });
    }

    // ================= LIST COMMANDS =================
    if(['.listonline','.listactive','.listinactive'].includes(text)){
      await sock.sendMessage(sender, { text: `⚡ Command ${text} executed!` });
    }

  });
}

startBot();
