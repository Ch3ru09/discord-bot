from tabnanny import check
import discord
import os
from dotenv import load_dotenv

from flask import Flask, request

load_dotenv()

# ---- Discord client --------------------------------------------
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def send(self, message, channel):
        for g in self.guilds:
            c = [ch for ch in g.text_channels if ch.name == channel]

            if not len(c) > 0:
                return
            
            await c.send(f"{message}")

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
            print(message.channel.id)
        
        if message.content == 'hi':
            await self.send("hi", "general")

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))

# ----------------------------------------------------------------

# ---- Messenger client ------------------------------------------
# app = Flask(__name__)
# @app.route('/', methods=['GET', 'POST'])
# def receive_message():
#     return "Hello World!"

# if __name__ == '__main__':
#     app.run()

# ----------------------------------------------------------------

# ---- main ------------------------------------------------------
# client.send("hi", "general")

# ----------------------------------------------------------------