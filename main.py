from flask import Flask, render_template
from flask_sock import Sock
import asyncio
import time
from telegram.App import App
from telegram.MessageMain import MessageSending
from telegram.Commands import Commands
from telegram.prase import Praser
from telegram.File import File
from AssembleAI.File_upload import Requests
from telegram.response import get_request

bot = App(command_prefix="!")


async def hello(ctx: Praser):
    ok = MessageSending()
    ok.text = 'hello'
    await ctx.message.replay(ok)


async def Audio(ctx: Praser):
    print(ctx.message.voice.file_id)
    ok = await get_request(f"https://api.telegram.org/bot{bot.token}/getFile?file_id={ctx.message.voice.file_id}")
    file = File(**ok['result'])
    path = file.file_path
    print(ok,path)
    audio = Requests("fbba59e571c74f05a80505312ff29917")
    ok = await audio.get_transcription(f"https://api.telegram.org/file/bot{bot.token}/{path}")
    status = 'queued'
    while status != 'queued':
        time.sleep(10)
        ok = await audio.get_result(id)
        print(ok)
        status = ok['status']


async def how_are_you(ctx: Praser):
    await ctx.message.replay("Fine")


Commands.add_command(hello)
Commands.add_command(Audio)
Commands.add_command(how_are_you)
bot.run(token="5764436314:AAHqvTxI4LLfkK6ilKC2Y4hEo-OW9-oM0g0")
