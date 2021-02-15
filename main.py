from instabot import Bot
import DatabaseHandler

bot = Bot()

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    print("TEST")
    cred=DatabaseHandler.extract_credetials('credentials.txt')
    conn=DatabaseHandler.create_connection(cred[2],cred[0],cred[1],cred[3])
    print(conn.is_connected())
