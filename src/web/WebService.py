from pyrebase import pyrebase
from psycopg2 import connect

firebaseConfig = {
    "apiKey": "AIzaSyDVdA0TB-zlPxdkzoh_Gxpynr_koHLWnGc",
    "authDomain": "miniprojectpythongame.firebaseapp.com",
    "projectId": "miniprojectpythongame",
    "storageBucket": "miniprojectpythongame.appspot.com",
    "messagingSenderId": "342094075809",
    "appId": "1:342094075809:web:6385d39bc01a7aad599de0",
    "measurementId": "G-397H9KP7RY",
    "databaseURL": ""
}

dbConfig = {
    'host': 'db-miniproject-konto-9925.aivencloud.com',
    'dbname': 'defaultdb',
    'user': 'avnadmin',
    'password': 'PyQCSrNfK2oEwFCd',
    'port': '22346'
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def login():
    print("Log in...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")

    except:
        print("Invalid email or password")

    finally:
        return connect_to_db()


def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        ask = input("Do you want to login?[y/n]")
        if ask == 'y':
            login()
    except:
        print("Email already exists")
    return

# returns status of disconnecting from the db
# TODO not sure if the line 'auth.current_user = None' is working
def logout(cursor, conn):
    auth.current_user = None
    return disconnect_from_db(cursor, conn)


def connect_to_db():
    conn, cursor = None, None
    try:
        conn = connect(
            host=dbConfig.get('host'),
            dbname=dbConfig.get('dbname'),
            user=dbConfig.get('user'),
            password=dbConfig.get('password'),
            port=dbConfig.get('port')
        )
        cursor = conn.cursor()
    except Exception as error:
        print(error)
    finally:
        return conn, cursor

# returns reference to db connection (conn) and the cursor for db which can be used to perform actions in the db
def disconnect_from_db(cursor, conn):
    code = None
    try:
        cursor.close()
        conn.close()
        code = 0
    except Exception as error:
        print(error)
        code = 1
    finally:
        return code

if __name__ == "__main__":
    conn, cursor = login()
    logout(conn, cursor)
