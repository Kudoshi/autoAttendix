import json
import telegram_send

# Run the setup_telegram.bat to setup the telegram bot link


# --- First time link telegram setup ---
#
# You only need to run it once
#
# How to link to telegram:
# 1. Speak with botfather in telegram and create a bot
# 2. Get bot token from botfather
# 3. Run telegrambot.py once
# 4. Give the token of the bot
# 5. A password will be given. Add your bot as a contact in telegram and send the password via the chat
# 6. If all goes well, a success message will be send in cmd and in telegram
# 7. Tadah you are done.
# Source: https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580

# -----------------------------------------------------------------------------------------------------------------



BOT_INFO_FILE = "./telegram_bot_config.txt"
CONFIG_FILE = "./config.json"

isLinkTelegram = False

# Checks the config file and loads the isLinkTelegram variable
def checkLinkStatus():

    data = json.loads(open(CONFIG_FILE, 'r').read())
    isLinkTelegram = data["linkTelegram"]
    if data["linkTelegram"] == "True":
        isLinkTelegram = True
    else:
        isLinkTelegram = False

def sendMessage(message):
    if (isLinkTelegram):
        telegram_send.send(messages=[message])



checkLinkStatus()

# Setup telegram link
if __name__ == '__main__':
    guideMessage = ("--- First time link telegram setup ---"
                    "\nYou only need to run it once"

                    "\n\nHow to link to telegram:"
                    "\n1. Speak with botfather in telegram and create a bot"
                    "\n2. Get bot token from botfather"
                    "\n3. Run telegrambot.py once"
                    "\n4. Give the token of the bot"
                    "\n5. A password will be given. "
                    "Add your bot as a contact in telegram and send the password via the chat"
                    "\n6. If all goes well, a success message will be send in cmd and in telegram"
                    "\n7. Tadah you are done.\n\n")
    print(guideMessage)

    # Config telegram_send process
    while(True):
        try:
            telegram_send.configure(BOT_INFO_FILE)
            isLinkTelegram = 'True'
        except:
            print("-" *100 + "\n")
            isLinkTelegram = 'False'


        configJSON = {
            "linkTelegram": isLinkTelegram
        }

        # Update Config.JSON with new link telegram value
        json_object = json.dumps(configJSON, indent=4)
        with open("config.json", "w") as outfile:
            outfile.write(json_object)

        if isLinkTelegram == "True":
            break


    if (isLinkTelegram):
        telegram_send.send(messages=["Account is linked to telegram successfully!"])