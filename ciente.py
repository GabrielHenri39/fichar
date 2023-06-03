import discord

class Client(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, intents=discord.Intents.default(),intents_message_content=True)
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced =True
        print(f'Entramos como \033[1;32m{self.user}\033[0m')
        
       

       

