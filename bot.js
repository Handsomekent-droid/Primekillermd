// bot.js
const fs = require('fs');
const path = require('path');
const utils = require('./utilis');
const antidelete = require('./primekillermd/antidelete');
const antilink = require('./primekillermd/antilink');
const group_commands = require('./primekillermd/group_commands');
const media = require('./primekillermd/media');
const bug_crash = require('./primekillermd/bug_crash');

// Initialize bot (replace this with actual WhatsApp bot instance)
const bot = utils.initBot({ sendMessage: console.log, listen: () => [] });

// Welcome / start message
function startMessage(userNumber) {
    const menu = utils.getMenu(userNumber);
    bot.sendMessage(userNumber, `Hello ${userNumber}!\n${menu}`);
}

// Handle commands
function handleCommand(userNumber, message) {
    const text = message.trim().toLowerCase();

    // Pairing
    if (text.startsWith('.pair')) {
        const number = text.split(' ')[1];
        if (!number) return bot.sendMessage(userNumber, 'Enter your phone number to pair e.g., 2547xxxxxxx');
        const success = utils.pairUser(number);
        return bot.sendMessage(userNumber, success ? `✅ Number ${number} paired successfully!` : '❌ Already paired.');
    }

    // Owner-only commands
    if (text.startsWith('.delpair')) {
        const success = utils.delPair(userNumber);
        return bot.sendMessage(userNumber, success ? '✅ All pairs deleted.' : '❌ You are not the owner.');
    }

    if (text.startsWith('.listpair')) {
        const list = utils.listPairs(userNumber);
        const formatted = list.length ? list.map(u => u.number).join('\n') : 'No pairs yet.';
        return bot.sendMessage(userNumber, `Paired Numbers:\n${formatted}`);
    }

    // Antidelete
    if (text.startsWith('.antidelete')) return antidelete.run(bot, message, userNumber);

    // Antilink
    if (text.startsWith('.antilink')) return antilink.run(bot, message, userNumber);

    // Group commands
    if (text.startsWith('.promote') || text.startsWith('.demote') || text.startsWith('.kickall') || text.startsWith('.close') || text.startsWith('.open')) {
        return group_commands.run(bot, message, userNumber);
    }

    // Media commands
    if (text.startsWith('.image') || text.startsWith('.video') || text.startsWith('.song') || text.startsWith('.tiktok') || text.startsWith('.yts') || text.startsWith('.vcf')) {
        return media.run(bot, message, userNumber);
    }

    // Bug / crash
    if (text.startsWith('.bug')) return bug_crash.run(bot, message, userNumber);

    // Ping
    if (text.startsWith('.ping')) return bot.sendMessage(userNumber, '🏓 Pong!');

    // Menu
    if (text.startsWith('.menu') || text.startsWith('.start')) return startMessage(userNumber);

    // Unknown command
    bot.sendMessage(userNumber, '❌ Unknown command. Use .menu to see all commands.');
}

// Main loop
function main() {
    // Replace with your bot.listen implementation
    const listeners = bot.listen(); // Example: [{user: '2547xxxxxxx', message: '.ping'}]
    for (const { user, message } of listeners) {
        handleCommand(user, message);
    }
}

// Start the bot
main();
