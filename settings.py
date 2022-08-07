import os

# MongoDB configuration
if os.getenv("MONGO_URI"):
    MONGO_URI = os.getenv("MONGO_URI")
else:
    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_PORT = int(os.getenv("MONGO_PORT"))
    MONGO_USERNAME = os.getenv("MONGO_USERNAME")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_AUTH_SOURCE = os.getenv("MONGO_AUTH_SOURCE")
MONGO_DBNAME = os.getenv("MONGO_DBNAME")

# Domain configuration
DOMAIN = {}
