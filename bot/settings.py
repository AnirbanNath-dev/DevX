from dotenv import load_dotenv
import os


load_dotenv()


TOKEN = os.environ["TOKEN"]
PREFIX = os.environ["PREFIX"]
COGS = ["Moderation" , "Music"]
WAVELINK_URI = os.environ["WAVELINK_URI"]
WAVELINK_PASS = os.environ["WAVELINK_PASS"]
