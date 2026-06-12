from dotenv import load_dotenv
import os

# Load .env file
load_dotenv("../.env")

# Application settings
APP_NAME = os.getenv("APP_NAME", "DevPulse")
DEBUG = os.getenv("DEBUG", "True") == "True"

# Database settings
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://u0_a836@localhost/devpulse"
)

# Security settings
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "devpulse-secret-key"
)

