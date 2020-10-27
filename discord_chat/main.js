const Discord = require("discord.js");
const client = new Discord.Client();

const flags = process.argv.slice(2);

// Check the message
const messagePos = flags.indexOf("-m");
if (messagePos === -1 || messagePos + 1 >= flags.length) {
  console.error("The message argument is needed!");
  process.exit(1);
}
const message = flags.slice(messagePos + 1).join(" ");

// Check the token
const tokenPos = flags.indexOf("-t");
if (tokenPos === -1 || tokenPos + 1 >= flags.length) {
  console.error("The token argument is needed!");
  process.exit(1);
}
client.login(flags[tokenPos + 1]);

client.on("ready", () => {
  // Check if there are any users or channels
  const userPos = flags.indexOf("-u");
  const channelPos = flags.indexOf("-c");

  if (channelPos === -1 && userPos === -1) {
    console.error("You have to specify either a user or a channel!");
    process.exit(1);
  }

  // Send messages to users
  if (userPos + 1 >= flags.length) {
    console.error("Please specify the users!");
    process.exit(1);
  } else {
    const users = flags[userPos + 1].split(",");
    for (let i = 0; i < users.length; i++) {
      client.users.cache.get(users[i]).send(message);
    }
  }

  // Send messages to channels
  if (channelPos + 1 >= flags.length) {
    console.error("Please specify the channels!");
    process.exit(1);
  } else {
    const channels = flags[channelPos + 1].split(",");
    for (let i = 0; i < channels.length; i++) {
      client.channels.cache.get(channels[i]).send(message);
    }
  }
});
