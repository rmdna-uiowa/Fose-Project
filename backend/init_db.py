import os
from config import Config
import mysql.connector
#from dotenv import load_dotenv

# Load environment variables
#load_dotenv()

# Database configuration

MYSQL_HOST = "localhost" #os.getenv('MYSQL_HOST', 'localhost')
# preferable to use a .env in our .gitignore so this info is actually secure, in which case we'd use the lines below instead:
# MYSQL_DB = os.getenv('MYSQL_DB', 'project_database')
# MYSQL_USER = os.getenv('MYSQL_USER', 'root')  # Root required for first-time setup
# MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
MYSQL_DB = "fose"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""

SHARED_USER = "project_user"
SHARED_PASSWORD = "secure_password"

# Connect to MySQL as root to set up the database and user - not done either
try:
  root_conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD  # Root password - may be empty in some local setups. 
  )
  root_cursor = root_conn.cursor()

  # Create the database if it doesn't exist
  root_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB};")

  # Create a project-specific user if it doesn't exist
  root_cursor.execute(f"CREATE USER IF NOT EXISTS '{SHARED_USER}'@'localhost' IDENTIFIED BY '{SHARED_PASSWORD}';")
  root_cursor.execute(f"GRANT ALL PRIVILEGES ON {MYSQL_DB}.* TO '{SHARED_USER}'@'localhost';")
  root_cursor.execute("FLUSH PRIVILEGES;")

  print(f"✅ Database '{MYSQL_DB}' and user '{SHARED_USER}' initialized successfully!")

  root_cursor.close()
  root_conn.close()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")