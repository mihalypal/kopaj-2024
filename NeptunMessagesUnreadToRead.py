from typing import List
import time
import requests

post_ids_number = 0     # store the number of unread messages

# The following functions are used to get the access token, get the unread messages, mark the messages as read

# get_access_token(username: str, password: str) -> tuple
# get_unread_messages(access_token: str, cookie: str) -> List[str]
# get_post_ids(access_token: str, message_id: str, cookie: str) -> str
# mark_messages_as_read(access_token: str, message_ids: List[str], cookie) -> None


def get_access_token(username: str, password: str) -> tuple:
    url = 'https://neptun.szte.hu/hallgato/api/Account/Authenticate'
    data = {
        "userName": username,
        "password": password,
        "captcha": "",
        "captchaIdentifier": "",
        "token": "",
        "LCID": 1038
    }
    response = requests.post(url, json=data)
    cookie = response.cookies
    # return the access token and the cookie if the username and password are correct, else return False
    return (response.json()['data']['accessToken'], cookie) if response.status_code == 200 else False


def get_unread_messages(access_token: str, cookie: str) -> List[str]:
    first_row = 0           # The number(id) of the first message to get
    last_row = 3000         # The number(id) of the last message to get
                            # If you have more than 3000 messages, you can increase this number
                            # The code will get the first 3000 messages -> [0, 3000], but you can change it if you want
    url = f'https://neptun.szte.hu/hallgato/api/Message/GetReceivedMessages?firstRow={first_row}&lastRow={last_row}&filterType=0'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Cookie': cookie
    }
    response = requests.get(url, headers=headers)
    unread_messages = [message for message in response.json()['data']['receivedMessages'] if message['unreadedPostCount'] != 0]
    unread_messages = [i['messageId'] for i in unread_messages]
    global post_ids_number
    post_ids_number = len(unread_messages)
    return unread_messages


def get_post_ids(access_token: str, message_id: str, cookie: str) -> str:
    url = f'https://neptun.szte.hu/hallgato/api/Message/GetMessagePosts?messageId={message_id}'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Cookie': cookie
    }
    response = requests.get(url, headers=headers)
    return response.json()['data']['posts'][0]['postId']


def mark_messages_as_read(access_token: str, message_ids: List[str], cookie) -> None:
    url = 'https://neptun.szte.hu/hallgato/api/Message/MarkMessagePostsAsReaded'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Cookie': cookie
    }
    global post_ids_number
    for message_id in message_ids:
        post_id = get_post_ids(access_token, message_id, cookie)
        data = {
            "messageId": f'{message_id}',
            "postIds": [f'{post_id}']
        }
        requests.post(url, json=data, headers=headers)
        print("Olvasatlan üzenetek száma:", post_ids_number)
        post_ids_number -= 1
        time.sleep(0.2)     # You can change this number if you get connection error or something like that (the value is in seconds)
    print("Olvasatlan üzenet id-k száma:", post_ids_number)
    print("Olvasatlan üzenetek olvasottá tétele sikeres!")


authentification = False


def main(username: str = '', password: str = ''):
    print("Add meg a Neptun kódod és jelszavad!")
    global authentification

    while not authentification:
        username = str(input("Neptun kód:\t\t")) if username == '' else username
        password = str(input("Neptun jelszó:\t")) if password == '' else password

        authentification = get_access_token(username, password)
        if username.lower() == 'x':
            return 0
        elif password.lower() == 'x':
            return 0
        elif not authentification:
            print("Hibás Neptun kód vagy jelszó! (Kilépéshez ezt írd be: 'x')")
            get_user_data()
    access_token, cookie = authentification

    print("Neptun üzenetek olvasottá tétele folymatban van...")

    cookie = cookie.values().__str__()
    cookie = cookie[1:-1].split(", ")
    cookie = [i[1:-1] for i in cookie]
    cookie = f"NEPTUN-LB={cookie[2]}; SERVER_HALLGATO={cookie[1]}; devicecookie-SzZRSlgx={cookie[0]}"

    unread_messages = get_unread_messages(access_token, cookie)
    mark_messages_as_read(access_token, unread_messages, cookie)


# main()

import tkinter as tk
from tkinter import CENTER

def get_user_data():
    def on_submit():
        username = entry_username.get()
        password = entry_password.get()
        root.destroy()
        res = main(username, password)
        if res == 0:
            return

    def on_enter(event):
        on_submit()
    
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x150+300+120")
    
    root.resizable(False, False)
    root.attributes("-alpha", 0.6)

    # Configure rows and columns for centering
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=0)  # Sor közti távolság csökkentése
    root.grid_rowconfigure(2, weight=0)
    root.grid_rowconfigure(3, weight=0)
    root.grid_rowconfigure(4, weight=1)  # Gomb alatti hely
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Username label and entry
    tk.Label(root, text="Username:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
    entry_username = tk.Entry(root)
    entry_username.grid(row=1, column=1, sticky="w", padx=5, pady=2)

    # Password label and entry
    tk.Label(root, text="Password:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=2, column=1, sticky="w", padx=5, pady=2)

    # Bind Enter key to password field
    entry_password.bind("<Return>", on_enter)

    # Submit button
    tk.Button(root, text="Submit", command=on_submit).grid(row=3, column=0, columnspan=2, pady=5)

    root.mainloop()


get_user_data()
