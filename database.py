from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Account, Password

class SessionManager:
    def __init__(self, db_file):
        engine = create_engine(f'sqlite:///{db_file}')
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def get_user(self):
        session = self.Session()
        user = session.query(User).first()
        session.close()
        return user

    def add_user(self, user):
        session = self.Session()
        session.add(user)
        session.commit()
        session.close()

    def add_account(self, account):
        session = self.Session()
        session.add(account)
        session.commit()
        session.close()

    def get_accounts(self, user_id):
        session = self.Session()
        accounts = session.query(Account).filter_by(user_id=user_id).all()
        session.close()
        return accounts

    def get_password(self, account_id):
        session = self.Session()
        password = session.query(Password).filter_by(account_id=account_id).first()
        session.close()
        return password

    def add_password(self, password):
        session = self.Session()
        session.add(password)
        session.commit()
        session.close()

    def update_password(self, session, account_id, new_password):
        password = session.query(Password).filter_by(account_id=account_id).first()
        if password:
            password.encrypted_password = new_password
            session.commit()

    def delete_account(self, session, account_id):
        account = session.query(Account).filter_by(id=account_id).first()
        if account:
            session.delete(account)
            session.commit()