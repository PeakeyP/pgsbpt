#!/usr/bin/python3

import discord

class PgsBot(discord.Client):
    async def on_ready(self):
        print('Logged in as {0}.'.format(self.user))

    async def on_message(self, message):
        print('<#{}> @{}: {}'.format(
                message.channel,
                message.author,
                message.content
        ))

        if message.author.id == self.user.id:
            return

        if message.content == '!ping':
            await message.channel.send('pong')

client = PgsBot()
client.run('API_KEY')
