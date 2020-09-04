import os

BASE_URL = os.getenv("BASE_URL")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
DEBUG_LOG_FILE = "/var/log/app_debug.log"
