import asyncio
import importlib

from pyrogram import idle
from Daxxhack import LOG
from Daxxhack.modules import ALL_MODULES


async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("Daxxhack.modules." + all_module)
    LOG.print("[bold yellow]𝐁𝐎𝐓 𝐒𝐓𝐀𝐑𝐓𝐄𝐃 𝐍𝐎𝐖")
    await idle() 
    LOG.print("[bold red]𝐂𝐀𝐍𝐂𝐋𝐄 𝐀𝐋𝐋 𝐓𝐀𝐒𝐊..........")



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
