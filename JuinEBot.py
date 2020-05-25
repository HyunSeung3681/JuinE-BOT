import discord
import asyncio
import os

app = discord.Client()

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("=============")
    messages = ["쮜뉘야 도움을 입력해보세요!", f"{len(app.guilds)}개의 서버와 함께", f"{len(app.users)}명의 유저와 함께"]
    while True:
        await app.change_presence(status=discord.Status.online, activity=discord.Activity(name=messages[0], type=discord.ActivityType.playing))
        messages.append(messages.pop(0))
        await asyncio.sleep(5)
    
@app.event
async def on_message(message) :
    if message.author.bot:
        return None
    if message.content == "쮜뉘야 도움":
        await message.channel.send("아직 만들고 있어요... 뚝딱뚝딱")
    if message.content == "쮜뉘야 hellothisisverification":
        if message.author.id == "285185716240252929":
            await message.channel.send("현승 | HyunSeung#3681")
        else:
            await message.channel.send("죄송하지만 원더님만 사용할 수 있게 쮜뉘님이 설정해놓으셨어요... 현승 | HyunSeung#3681로 DM을 주시면 최대한 빨리 해놓을겁니다!")

access_token=os.environ["BOT_TOKEN"]
app.run(access_token)
