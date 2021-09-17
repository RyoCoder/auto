import asyncio
import time
from telethon import events
from telethon.sync import TelegramClient
from telethon import functions, types

api_id = 4715844
api_hash = 'bfff18a8e96d5b64c3ee54593de7b331'
phone = '84589467867'
ryostar = 'ryostar'
password = '#' 

# content of the automatic reply
message = "Hello There!\n\nSorry I am currently Busy." \
          "\nYour message will be responded when I am free, Thanks"

def main():

    client = TelegramClient(ryostar, api_id, api_hash, sequential_updates=True)


    @client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
    async def _(event):
        sender = await event.get_sender()
        first_name = sender.first_name
        await event.respond('**Chào** ' + first_name + message)

    #===========================================================================================#
    print(time.asctime(), '-', 'Auto Replying is Started')
    client.start(phone, password)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Auto Replying is Stopped!')
    #===========================================================================================#

if __name__ == '__main__':
    main()
