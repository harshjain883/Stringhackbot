import os
import asyncio
import logging

from pyrogram import Client
from pyromod import listen
from rich.console import Console
from rich.table import Table

import config
from Daxxhack.Helpers.data import LOG_TEXT


#rich
LOG = Console()
START_PIC = config.START_PIC

#logger
logging.basicConfig(level=logging.INFO)

#client
app = Client(
    name="SessionHack",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.TOKEN,
    in_memory=True,
)

async def Daxxhack():
    os.system("clear")
    header = Table(show_header=True, header_style="bold green")
    header.add_column(LOG_TEXT)
    LOG.print(header)
    LOG.print(f"[bold cyan]𝐌𝐑.𝐃𝐀𝐗𝐗")
    LOG.print("[bold yellow]𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭.............")
    await app.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(Daxxhack())
