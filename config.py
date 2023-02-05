import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23990433")

API_HASH = os.environ.get("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5964494060:AAFfOEerT8lR8YqyEHJQtbFQidqkqkYUaO8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "SK_MoviesOffl") 

DB_NAME = os.environ.get("DB_NAME","sk")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Test:1234@cluster0.2bzsp0q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
