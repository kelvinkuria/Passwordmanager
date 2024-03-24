Password Manager CLI Application
This is a command-line interface (CLI) application for managing passwords, built using Python. It allows users to securely store, retrieve, update, and delete account credentials. The application follows best practices and utilizes SQLite database, SQLAlchemy ORM, and the cryptography library for password encryption and decryption.

Features
Secure Password Storage: Passwords are encrypted using the Fernet encryption algorithm from the cryptography library before being stored in the SQLite database.
User Authentication: Users are authenticated using a master password, which is used to derive a key for encrypting and decrypting account passwords.
Account Management: Users can add, view, update, and delete account credentials (website, username, and password) through the CLI interface.
SQLite Database with SQLAlchemy ORM: The application uses a SQLite database to store user information, accounts, and passwords. SQLAlchemy ORM is used to interact with the database, providing an abstraction layer and simplifying database operations.
Virtual Environment with Pipenv: Pipenv is used to manage the project dependencies and ensure a consistent development environment.
Proper Package Structure: The application follows a modular design with separate modules for CLI, database operations, models, and utilities.
Installation
Clone the repository:


git clone https://github.com/your-username/password-manager-cli.git
Navigate to the project directory:


cd password-manager-cli
Install dependencies using Pipenv:


pipenv install
Activate the virtual environment:


pipenv shell
Usage
Run the application:


python main.py
Enter a master password when prompted (or create a new user if none exists).
Follow the CLI menu options to add, view, update, or delete accounts and passwords.
Code Structure
The project consists of the following files and modules:

main.py: The entry point of the application, which launches the CLI interface.
cli.py: Contains the PasswordManagerCLI class, which handles user interaction and CLI menu display.
database.py: Defines the SessionManager class, which manages database operations using SQLAlchemy ORM.
models.py: Contains SQLAlchemy models for the User, Account, and Password tables.
utils.py: Provides utility functions for password encryption, decryption, and key derivation.
Dependencies
The following dependencies are required for running the application:

SQLAlchemy
cryptography
These dependencies are automatically installed when running pipenv install.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Acknowledgments
The cryptography library for providing secure password encryption and decryption functionality.
SQLAlchemy for the powerful ORM and database abstraction layer.
Pipenv for managing project dependencies and virtual environments.
