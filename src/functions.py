import os
from config import FOLDER_PATH, BACKUP_FOLDER_PATH, MAX_BACKUP_AMOUNT, BACKUP_FREQUENCY
from datetime import date
import zipfile
from pathlib import Path

def backup_management():
    bu_path = Path(BACKUP_FOLDER_PATH)
    to_bu = Path(FOLDER_PATH)
    try:
        existing_backups = [f for f in bu_path.iterdir() if f.is_file()]
        existing_backups.sort(key=lambda x: os.path.getmtime(x))
        date_last_backup = date.fromtimestamp(os.path.getmtime(existing_backups[-1]))
        date_delta = date.today() - date_last_backup
        date_delta = date_delta.days
        msg = f'{date_delta} days since last backup.'
    except IndexError:
        date_delta = 31
        msg = 'No backups found.'
    if date_delta > BACKUP_FREQUENCY:
        backup_approval = input(f'{msg}\n\tDo you want to BACKUP NOW? (y/n) ')
        if backup_approval == 'y':
            backup_name = f'backup.{date.today()}.{to_bu.name}.zip'
            zip_file = zipfile.ZipFile(BACKUP_FOLDER_PATH + backup_name, 'w')
            for file in to_bu.glob('**/*'):
                if file.is_file():
                    zip_file.write(
                        file.absolute(),
                        arcname=str(file.relative_to(to_bu)),
                        compress_type=zipfile.ZIP_DEFLATED
                    )
            zip_file.close()
            existing_backups = [f for f in bu_path.iterdir() if f.is_file()]
            existing_backups.sort(key=lambda x: os.path.getmtime(x))
            while len(existing_backups) > MAX_BACKUP_AMOUNT:
                os.remove(existing_backups[0])
                existing_backups.pop(0)
        elif msg == 'No backups found.':
            print(f'DANGER: There are no backups. Backup asap.\nTHE END')
        else:
            print(f'{date_delta} days since last backup. Backup asap.\nTHE END')
    else:
        print(f'{date_delta} days since last backup. Skipping.\nTHE END')