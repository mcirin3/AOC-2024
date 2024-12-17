import os
from dotenv import load_dotenv

# Load session cookie from .env file
load_dotenv()
session_cookie = os.getenv("SESSION_COOKIE")