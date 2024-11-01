import sys
import json
import sqlite3

def main():
    # Load the data
    json_args = sys.argv[1]
    args = json.loads(json_args)

    function_name = args['function_name']
    username = args['username']
    email = args['email']
    password = args['password']
    return 0

def confirm_db_connection():
    # Confirm the database connection

    conn = sqlite3.connect('./assets/local-data/user_accounts.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
        )
        '''
    )
    conn.commit()
    conn.close()
    print('urubu')

def register(username, email, password):
    # Register the user
    pass

if __name__ == '__main__':
    main()
    confirm_db_connection()
    print('Success')

