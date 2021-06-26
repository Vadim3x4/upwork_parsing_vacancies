
# Upwork vacancies to chat Telegram

The script parses the page specified in "URL_TO_PARSE" (this url can be obtained using the Upwork search). After receiving the page data, the script takes out the data (Title, Link, Price), and sends them to the telegram chat "CHAT_ID"specified by you.

##  Installation.

### 1. Installing PIP Dependencies:
```bash
# Using pip
pip install requirements.txt
# Using pip3
pip3 install requirements.txt
```

### 2. Add your data to the config file:
  #### 2.1 To get the API token, create a Telegram bot. To do this, contact @BotFather in the Telegram, and write /start, follow the instructions.
  #### 2.2 To get the CHAT_ID, contact @userinfobot in the Telegram, and write any message, follow the instructions.
  #### 2.2 According to the standard, the polling time is 5 minutes, you can certainly reduce it in the "SLEEP_TIMER" variable (or have mercy on the Upwork server). But be prepared for blocking requests from your IP. To bypass it, you can use a proxy in requests.

```bash
{
    "headers":{
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0"
    },
    "telegram_token":"YOUR_TELEGRAM_API_TOKEN",
    "chat_id":"YOUR_CHAT_ID"
}
```


### 3. Running the script:
```bash
python main.py
or
python3 main.py
```

## Technology Stack: Python 3.8.5, BeautifulSoup4, Lxml, Requests.

## Author [Vadim3x4](https://github.com/Vadim3x4)  Email: kurnuli2010@yandex.ru Telegram: @Kurnuli3x4


