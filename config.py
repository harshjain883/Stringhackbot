import os
from dotenv import load_dotenv

load_dotenv()


API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
TOKEN = os.getenv("TOKEN", None)
START_PIC = "https://telegra.ph/file/2dcb2ea8da198a5507df7.jpg"
