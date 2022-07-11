import os

from dotenv import load_dotenv
load_dotenv()

FOLDER_PATH = os.environ.get('FOLDER_PATH')
BACKUP_FOLDER_PATH = os.environ.get('BACKUP_FOLDER_PATH')
MAX_BACKUP_AMOUNT = int(os.environ.get('MAX_BACKUP_AMOUNT'))
BACKUP_FREQUENCY = int(os.environ.get('BACKUP_FREQUENCY'))