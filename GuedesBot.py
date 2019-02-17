import discord
import asyncio
import os
from discord.utils import get

client = discord.Client()

@client.event
async def on_ready():
	discord.utils.get(client.get_all_emojis())

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='AIDS', url='https://twitch.tv/$', type=1))
    print('to funcionando essa merda')

@client.event
async def on_message(text):
    if (text.author.id == 'ID DO BOT'): return    
    if text.content.startswith('gb!'):
        usertxt = text.content[3:].strip()
        if usertxt.lower().startswith('nescau'):
                        answer = '<:nescau:499511375710781450>'
                        await client.send_message(text.channel,answer)
                        return
                
        if usertxt.lower().startswith('nesquik'):
                        answer = '<:nesquik:499886751872057375>'
                        await client.send_message(text.channel,answer)
                        return

        if usertxt.lower().startswith('todd'):
                        toddyscrim = text.content[7:].strip()
                        if toddyscrim.lower().endswith('y'):
                                answer = '<:toddy:499514309970362368>'
                                await client.send_message(text.channel,answer)
                                return
                        
                        if toddyscrim.lower().startswith('ynho'):
                                answer = '<:toddynho:545798860484640778>'
                                await client.send_message(text.channel,answer)
                                return
                        return

        if usertxt.lower().startswith('toddynho'):
                        answer = '<:toddynho:545798860484640778>'
                        await client.send_message(text.channel,answer)
                        return
		
        if usertxt.lower().startswith('whey'):
                        answer = '<:whey:522629683586662415>'
                        await client.send_message(text.channel,answer)
                        return

        if usertxt.lower().startswith('help'):
                        answer = 'Este é o **GuedesBotBeta**. Se o conteúdo do GuedesBotBeta for o mesmo que o do **GuedesBot**, isso significa que a ele está estável suficiente para o uso!\nCaso precisar da lista inteira de comandos, envie `gb!list`. Para informações sobre a build atual do GuedesBot, envie `gb!info`.'
                        await client.send_message(text.channel,answer)
                        return

        if usertxt.lower().startswith('list'):
                        answer = '```gb!nesquik - Envia um :nesquik:\ngb!nescau - Envia um :nescau:\ngb!toddynho - Envia um :toddynho:\ngb!toddy - Envia um :toddy:\ngb!help - Exibe informações sobre "por que tem dois GuedesBots e por que eles talvez tenham os exatos mesmos comandos?"\ngb!info - Exibe informações sobre o bot\ngb!changelog - Exibe a lista de mudanças feitas a partir da v1.2.5beta\ngb!list - Exibe essa lista```'
                        await client.send_message(text.channel,answer)
                        return


        if usertxt.lower().startswith('info'):
                        answer = '**O GuedesBotBeta está operando normalmente.** `v1.2.8beta 15/02/2019 04:22 GMT-2`\nPara ver o changelog, digite `gb!changelog`'
                        await client.send_message(text.channel,answer)
                        return
		
        if usertxt.lower().startswith('changelog'):
                        answer = '```v1.2.8.2beta - 17/02/2019 - 18:23 GMT-3\n\n- Bot agora conta com "usertxt" substituindo o "frase", a fim de manter com seus comandos em inglês.\n\nv1.2.8.1beta - 16/02/2019 04:34 GMT-2\n- Bot agora com seus comandos em inglês, facilitando suas operações.\n\nv1.2.8beta - 15/02/2019 07:30 GMT-2\n- Bot transferido para a Google Cloud.\n\nv1.2.5beta - 15/02/2019 04:22 GMT-2\n- Adicionado gb!whey.\n- Bot rodando na nuvem Heroku.```'
                        await client.send_message(text.channel,answer)
                        return

client.run('TOKEN')
