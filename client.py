import asyncio
from telethon import TelegramClient, events
from telethon import functions, types
from telethon.tl.functions.contacts import ResolveUsernameRequest


api_id = 16730216
api_hash = '7149151835bfc915b7b3c0d883c35a0f'
chat_list = {
  1510807748, #dio_test1
  1761727648, #Yulia Stupak
  1026808817, #Голый спорт
  1775876018, #Вероника Степанова ⛷
  1160254506, #Лыжная классика
  1770780054, #Российские лыжи
  1566128939, #SanSanychBolshunov
  1179136741, #ROMANOV
  1414344822, #Ски Доуп
  1630427251, #Александр Легков
  1659241562, #Максим Вылегжанин
  1416614413  #Ирина Коваленко

}
client = TelegramClient('rus-ski', api_id, api_hash)
target_channel = None;



@client.on(events.NewMessage)
async def my_event_handler(event):
  #print(event.stringify())
  chat = await event.get_chat()
  if (chat.id in chat_list):
    print(f'Channel: {chat.title}, message: {event.message.message}')
    await client.forward_messages(target_channel, event.message)

def get_target_channel(channel_id):
  for dialog in client.iter_dialogs():
    if dialog.is_channel and dialog.entity.id==channel_id:
      print(f'target channel is set: {dialog.entity.id} {dialog.entity.title}')
      return dialog.entity

  
client.start()
target_channel = get_target_channel(1510807748)
client.run_until_disconnected()
    
 



