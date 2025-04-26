from telethon import TelegramClient, events
api_id = 25427477
api_hash = 'b56a45ea769195ee0fc173f0850d4805'
client = TelegramClient('sessions', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi! i am monu mishra from gaya')
    elif 'monu' in event.raw_text:
        await event.reply("i am monu mishra here\n what i can do for you?")
    else :
        await event.reply('hey what are yiu looking for?')

client.start()
client.run_until_disconnected()