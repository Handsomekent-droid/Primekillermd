const fs = require('fs');
const path = require('path');
const PAIRS_FILE = path.join(__dirname, 'pairs.json');

// Config
const OWNER_NUMBER = "254792770219"; // Only owner can use delpair/listpair
const WHATSAPP_CHANNEL = "https://whatsapp.com/channel/0029Vb7UKYqHbFVCW3uGad0l";
const TELEGRAM_CONTACT = "https://t.me/Handsome_primis_killer_kent";

// Initialize pairs.json if not exists
if (!fs.existsSync(PAIRS_FILE)) {
    fs.writeFileSync(PAIRS_FILE, JSON.stringify({ pairs: [] }, null, 2));
}

module.exports = {

  // Initialize bot (replace with actual WhatsApp bot init)
  initBot: function(botInstance) {
    console.log("⛧ＰＲＩＭΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ ɃЦ₲ ɃØŦ is running...");
    console.log("Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧");
    return botInstance;
  },

  // Load current pairs
  loadPairs: function() {
    const data = fs.readFileSync(PAIRS_FILE);
    return JSON.parse(data);
  },

  // Save pairs
  savePairs: function(data) {
    fs.writeFileSync(PAIRS_FILE, JSON.stringify(data, null, 2));
  },

  // Pair user
  pairUser: function(number) {
    const pairs = this.loadPairs();
    if (pairs.pairs.find(u => u.number === number)) return false;
    pairs.pairs.push({ number, paired: true });
    this.savePairs(pairs);
    return true;
  },

  // Delete all pairs (owner only)
  delPair: function(requesterNumber) {
    if (requesterNumber !== OWNER_NUMBER) return false;
    const pairs = this.loadPairs();
    pairs.pairs = [];
    this.savePairs(pairs);
    return true;
  },

  // List all pairs (owner only)
  listPairs: function(requesterNumber) {
    if (requesterNumber !== OWNER_NUMBER) return [];
    const pairs = this.loadPairs();
    return pairs.pairs;
  },

  // Generate menu for a user
  getMenu: function(userNumber) {
    const menu = `
╭━━ ◇「 ° PRIME KILLER MD BOT ° 」◇
┃⌬ BOT : ⛧ＰＲＩＭΞ⛧ ᛕΙᄂᄂΞＲ ⛧CЯΛSᕼΞЯ⛧ ɃЦ₲ ɃØŦ
┃⌬ OWNER : ${OWNER_NUMBER}
┃⌬ PLATFORM : WhatsApp
┃⌬ CONTACT : ${TELEGRAM_CONTACT}
╰━━━━━━━━━━━━━━━◇

╭━━ ◇「 COMMANDS 」◇
┃⌬ .pair <your_number> - Pair your WhatsApp number
┃⌬ .delpair - Delete all pairs (Owner only)
┃⌬ .listpair - List all paired numbers (Owner only)
┃⌬ .antidelete - Anti delete messages
┃⌬ .antilink - Anti link messages
┃⌬ .promote / .demote / .kickall - Group admin commands
┃⌬ .image / .video / .song / .tiktok / .yts - Media commands
┃⌬ .bug - Bug / Crash (COMING SOON)
┃⌬ .ping - Bot ping test
╰━━━━━━━━━━━━━━━◇

🔗 WhatsApp Channel: ${WHATSAPP_CHANNEL}
🔗 Telegram Contact: ${TELEGRAM_CONTACT}

Powered by ⛧ＰＲＩΜΞ⛧ kîᄂᄂér ⛧ƘΞИŦ⛧
`;
    return menu;
  }
};
