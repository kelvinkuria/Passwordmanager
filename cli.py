import getpass
from models import Account, Password

class PasswordManagerCLI:
    def __init__(self, session_manager, fernet):
        self.session_manager = session_manager
        self.fernet = fernet

    def run(self):
        user = self.session_manager.get_user()
        while True:
            print("\nPassword Manager")
            print("1. Add Account")
            print("2. View Accounts")
            print("3. Update Password")
            print("4. Delete Account")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_account(user.id)
            elif choice == "2":
                self.view_accounts(user.id)
            elif choice == "3":
                self.update_password(user.id)
            elif choice == "4":
                self.delete_account(user.id)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.")

    def add_account(self, user_id):
        website = input("Enter website: ")
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        encrypted_password = self.fernet.encrypt(password.encode())

        session = self.session_manager.Session()
        account = Account(website=website, username=username, user_id=user_id)
        session.add(account)
        session.flush()  # Flush the session to get the account.id

        password_entry = Password(account_id=account.id, encrypted_password=encrypted_password)
        session.add(password_entry)
        session.commit()  # Commit both the account and password
        session.close()

        print("Account added successfully.")

    def view_accounts(self, user_id):
        session = self.session_manager.Session()
        accounts = session.query(Account).filter_by(user_id=user_id).all()
        session.close()

        if not accounts:
            print("No accounts found.")
            return

        print("\nAccounts:")
        for account in accounts:
            session = self.session_manager.Session()
            password = session.query(Password).filter_by(account_id=account.id).first()
            if password:
                decrypted_password = self.fernet.decrypt(password.encrypted_password).decode()
                print(f"Website: {account.website}, Username: {account.username}, Password: {decrypted_password}")
            else:
                print(f"Website: {account.website}, Username: {account.username}, Password: (No password set)")
            session.close()

    def update_password(self, user_id):
        session = self.session_manager.Session()
        accounts = session.query(Account).filter_by(user_id=user_id).all()
        session.close()

        if not accounts:
            print("No accounts found.")
            return

        print("\nAccounts:")
        for i, account in enumerate(accounts, start=1):
            print(f"{i}. Website: {account.website}, Username: {account.username}")

        choice = int(input("Enter the account number to update password: "))
        if choice < 1 or choice > len(accounts):
            print("Invalid choice.")
            return

        account = accounts[choice - 1]
        new_password = getpass.getpass("Enter new password: ")
        encrypted_password = self.fernet.encrypt(new_password.encode())

        session = self.session_manager.Session()
        self.session_manager.update_password(session, account.id, encrypted_password)
        session.close()

        print("Password updated successfully.")

    def delete_account(self, user_id):
        session = self.session_manager.Session()
        accounts = session.query(Account).filter_by(user_id=user_id).all()
        session.close()

        if not accounts:
            print("No accounts found.")
            return

        print("\nAccounts:")
        for i, account in enumerate(accounts, start=1):
            print(f"{i}. Website: {account.website}, Username: {account.username}")

        choice = int(input("Enter the account number to delete: "))
        if choice < 1 or choice > len(accounts):
            print("Invalid choice.")
            return

        account = accounts[choice - 1]
        session = self.session_manager.Session()
        self.session_manager.delete_account(session, account.id)
        session.close()

        print("Account deleted successfully.")