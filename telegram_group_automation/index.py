# Import telegram python api
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.contacts import DeleteContactsRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.messages import GetDialogsRequest

# Import configuration file
import toml

# Helpers
import sys
import csv
import random
from rich.console import Console

# Load configuration file
config = toml.load('config.toml')
console = Console()

# Initialize Telegram config
api_id = config['telegram']['api_id']
api_hash = config['telegram']['api_hash']
phone = config['telegram']['phone']
client = TelegramClient(phone, api_id, api_hash)
client.connect()
# Arbitrary variables
input_file = sys.argv[1]

# Check if auth is successful
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

# Enter csv file
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['phonenumber'] = row[0]
        user['firstname'] = row[1]
        user['lastname'] = row[2]
        users.append(user)

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash=0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        groups.append(chat)
    except Exception as e:
        print(e)
        continue

console.print('Choose a group to add members:', style="bold green")
i = 0
for group in groups:
    console.print(str(i) + ' - ' + group.title, style="bold blue")
    i += 1

console.print("Enter a Group Number: ", style='bold green')
g_index = input()
target_group = groups[int(g_index)]

for user in users:
    try:
        # add user to contact
        contact = InputPhoneContact(
            client_id=random.randrange(-2**63, 2**63),
            phone=user['phonenumber'],
            first_name=user['firstname'],
            last_name=user['lastname']
        )
    except Exception as e:
        console.print(
            'Could not create user : ' + user['firstname'] + ' Error : ' + e,
            style='bold red'
        )

    try:
        result = client(ImportContactsRequest([contact]))
        print(result)
        client(AddChatUserRequest(
                user_id=result.users[0],
                fwd_limit=0,
                chat_id=target_group.id
            )
        )
        client(DeleteContactsRequest(id=result.users))
    except Exception as e:
        console.print(
            str(e) + ' - ' + user['firstname'],
            style='bold red'
        )
