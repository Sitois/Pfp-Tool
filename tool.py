import requests
import base64
from colorama import Fore, Style, Back

print(Fore.LIGHTGREEN_EX + """ _______    ______                 ________                   __ 
/       \  /      \               /        |                 /  |
$$$$$$$  |/$$$$$$  |______        $$$$$$$$/______    ______  $$ |
$$ |__$$ |$$ |_ $$//      \          $$ | /      \  /      \ $$ |
$$    $$/ $$   |  /$$$$$$  |         $$ |/$$$$$$  |/$$$$$$  |$$ |
$$$$$$$/  $$$$/   $$ |  $$ |         $$ |$$ |  $$ |$$ |  $$ |$$ |
$$ |      $$ |    $$ |__$$ |         $$ |$$ \__$$ |$$ \__$$ |$$ |
$$ |      $$ |    $$    $$/          $$ |$$    $$/ $$    $$/ $$ |
$$/       $$/     $$$$$$$/           $$/  $$$$$$/   $$$$$$/  $$/ 
                  $$ |                                           
                  $$ |                                           
                  $$/                                            """, Style.RESET_ALL)


token = input("Bot Token: ")
path_pfp = input("New animated avatar Path: ")

def update_avatar():
    try:
        with open(path_pfp, 'rb') as file:
            new_avatar = file.read()

        headers = {
            'Authorization': f'Bot {token}',
            'Content-Type': 'application/json'
        }

        avatar_base64 = base64.b64encode(new_avatar).decode('utf-8')
        body = {
            'avatar': f'data:image/gif;base64,{avatar_base64}'
        }

        response = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json=body)

        if response.ok:
            print(Fore.GREEN, "[+]", Fore.LIGHTGREEN_EX + 'Avatar updated successfully!', Style.RESET_ALL)
            print(Fore.GREEN, "[!!!]", Fore.LIGHTGREEN_EX + 'don\'t forget to leave a star! (https://github.com/Sitois/Pfp-Tool)', Style.RESET_ALL)            
        else:
            print(Fore.RED, "[!]", Fore.LIGHTRED_EX, 'Failed to update avatar:', response.status_code)
            print('Response body:', response.text, Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED, "[!]", Fore.LIGHTRED_EX, 'Error while updating avatar:', e, Style.RESET_ALL)

update_avatar()