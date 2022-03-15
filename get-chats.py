import asyncio
from telethon import TelegramClient, events
from telethon import functions, types
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import Channel, Chat


api_id = 16730216
api_hash = '7149151835bfc915b7b3c0d883c35a0f'

client = TelegramClient('rus-ski', api_id, api_hash)

 
async def main():
    async for dialog in client.iter_dialogs():
      if isinstance(dialog.entity, Channel): 
        entity = dialog.entity
        if hasattr(entity, "name"):
          print(f'{type(entity)} {entity.name}: {entity.id}')
        if hasattr(entity, "title"):
          print(f'{entity.id}, #{entity.title}')
      

with client:
    client.loop.run_until_complete(main())
    
 



