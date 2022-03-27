from pyrebase import pyrebase
from psycopg2 import connect

# Works on Python 3.8.0
# For pyrebase install use: pip install pyrebase4
# pip version 22.0.4


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


class User:
    def __init__(self):
        self.nick = None
        self.email = None
        self.sex = None
        self.age = None
        self.UID = None

    def login(self, email, password):
        try:
            login = auth.sign_in_with_email_and_password(email, password)
            conn, cursor = connect_to_db()
            cursor.execute("SELECT * FROM players WHERE uid = %s;", (login['localId'],))
            user = cursor.fetchall()[0]
            self.nick = user[0]
            self.email = user[1]
            self.sex = user[2]
            self.age = user[3]
            self.UID = user[5]
            disconnect_from_db(conn, cursor)

            print("Successfully logged in!")

        except:
            print("Invalid email or password")

    def signup(self, email, password, nick, sex, age):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            login = auth.sign_in_with_email_and_password(email, password)
            self.logout()
            conn, cursor = connect_to_db()

            cursor.execute("CALL add_player(%s ,%s , %s, %s, %s)", (nick, email, sex, age, login['localId']))
            conn.commit()

            disconnect_from_db(conn, cursor)

        except:
            print("Email already exists")

    # TODO may need further implementation
    def logout(self):
        auth.current_user = None


# returns reference to db connection (conn) and the cursor for db which can be used to perform actions in the db
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


def disconnect_from_db(conn, cursor):
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

