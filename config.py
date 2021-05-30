from dotenv import dotenv_values
import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv("PORT", 5000)
