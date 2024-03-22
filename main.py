# main.py
import os
import getpass
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

from models import User, Account, Password
from database import SessionManager
from cli import PasswordManagerCLI
def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password))

def main():
    db_file = os.path.join(os.path.dirname(__file__), 'password_manager.db')
    session_manager = SessionManager(db_file)

    while True:
        master_password = getpass.getpass("Enter master password: ").encode()
        user = session_manager.get_user()

        if user:
            salt = user.salt
            key = derive_key(master_password, salt)

            if key == user.master_password:
                break
        else:
            salt = os.urandom(16)
            key = derive_key(master_password, salt)
            user = User(master_password=key, salt=salt)
            session_manager.add_user(user)
            break

    fernet = Fernet(key)
    cli = PasswordManagerCLI(session_manager, fernet)
    cli.run()

if __name__ == "__main__":
    main()