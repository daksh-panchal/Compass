import os
from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
if not NOTION_API_KEY:
    raise RuntimeError("NOTION_API_KEY not found")

notion = Client(auth=NOTION_API_KEY)

