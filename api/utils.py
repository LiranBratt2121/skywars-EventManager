from dotenv import load_dotenv
import os

def get_hypixel_api_key() -> str:
    load_dotenv()
    return os.getenv('HYPIXEL_API_KEY')
