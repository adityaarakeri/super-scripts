# Discord Chat

This script allows you to send a message through a bot to someone or some channel.

## Instructions

Since this script is written in Javascript, you'll need to do `npm install` first. After that run `node main.js` with
the correct flags:

### Flags

- `-t <token>` - The bot's token
- `-u <user id(s)>` - The id of all the user you want to send a message to. If you are sending a message to multiple
  users, seperate them with `,` and without spaces, like this: `<userid1>,<userid2>,<userid3>`
- `-c <channel id(s)>` - The id of all the channels you want to send a message to. To send to multiple channel, use the
  same syntax defined for the users.
- `-m <message to send>` - This argument has to be in the end, since it might contain spaces
