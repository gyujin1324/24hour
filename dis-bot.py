from typing import Text
import discord, asyncio

from discord import message
from discord.embeds import Embed
from discord.enums import ContentFilter

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("썸네일,쇼츠 오버레이 구매 접수"))

@client.event
async def on_message(message):
    if message.content == "인증": # 메세지 감지
        await message.channel.send ("{} | {}, DM을 확인해주세요".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, 구매할 양식의 번호 실명 이메일 순으로 보내주세요".format(message.author, message.author.mention))
    if message.content == "!구매신청":
        embed = discord.Embed(title="썸네일", description="이 채팅 채널에 양식에 맞게 글을 써주세요\n\n\n양식\n\n원하시는 썸네일 번호:\n썸네일에 적힐 닉네임:\n이메일주소:\n실명:\n입금날짜:\n\n\n\n____________________",color=0x62c1cc)
        embed.set_footer(text="위에서부터 순서대로 1,2,3번\n썸네일에 로고를 넣으시고 싶으면 디엠 주세요!!\n※계좌:302-1606-2532-81※\n가격은 장당2000원입니다!!\n※궁금한 점은 개인 디엠!!")
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_image(url="")
        await message.channel.send("{} | {}, " .format(message.author, message.author.mention), embed=embed)
        await message.channel.send("https://cdn.discordapp.com/attachments/699809619010256986/801282988670189649/62df2b124f732bf6.gif")
        await message.channel.send("https://cdn.discordapp.com/attachments/744082872339660880/903525598046081044/abb905dfb140817b.png")
        await message.channel.send("https://cdn.discordapp.com/attachments/699809619010256986/801282988670189649/62df2b124f732bf6.gif")
        await message.channel.send("https://cdn.discordapp.com/attachments/744082872339660880/903525401110917190/1.png")
        await message.channel.send("https://cdn.discordapp.com/attachments/699809619010256986/801282988670189649/62df2b124f732bf6.gif")
        await message.channel.send("https://cdn.discordapp.com/attachments/744082872339660880/903525614085091328/x.png")
        await message.channel.send("https://cdn.discordapp.com/attachments/699809619010256986/801282988670189649/62df2b124f732bf6.gif")

    if message.content.startswith ("!청소"):
            i = (message.author.guild_permissions.administrator)

            if i is True:
                amount = message.content[4:]
                await message.channel.purge(limit=1)
                await message.channel.purge(limit=int(amount))

                embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0xD03625)
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.set_footer(text="", icon_url="")
                await message.channel.send(embed=embed)
            
            if i is False:
                await message.channel.purge(limit=1)
                await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))








# 봇을 실행시키기 위한 토큰을 작성해주는 곳  
client.run('OTAzMjUzNTM4OTA4NTYxNDE4.YXqSaQ.B89qrh_8EPYoA4ljEBRY0WnyTOQ')