import requests
import time
import json

from bs4 import BeautifulSoup


with open('config.json', 'r') as f:
    config = json.load(f)

HEADERS = config['headers']
TELEGRAM_TOKEN = config['telegram_token']
CHAT_ID = config['chat_id']
URL_TO_PARSE = 'https://www.upwork.com/ab/jobs/search/?q=Web%20scraping&sort=recency'
SLEEP_TIMER = 300


def parse() -> dict or None:
    """
    The function makes a request to the platform (Upwork),
    for a given page in "URL_TO_PARSE".
    It collects data from it, parses vacancies,
    and sends the incoming job to you in Telegram.
    """

    query = requests.get(
        URL_TO_PARSE,
        headers=HEADERS
    )
    if query.status_code != 200:
        time.sleep(180)
        return None

    soup = BeautifulSoup(query.text, 'lxml')
    job_list = soup.find_all(
        'section',
        attrs={"data-ng-if": "!loadingSpinner"}
    )
    if not job_list:
        return None

    data = {}
    for job in job_list:
        title = job.find('h4').text.strip()
        link = 'https://www.upwork.com' + job.find('a')['href']
        try:
            price = job.find('strong', class_='js-budget').text.strip()
        except AttributeError:
            try:
                price = job.find('strong').text.strip()
            except AttributeError:
                price = "Not specified"
        data[title] = (link, price)
    return data


def main():
    current_data = None
    while True:
        now_data = parse()
        if current_data is None:
            current_data = now_data
            continue

        for job, description in now_data.items():
            if job not in current_data:
                text = (
                    f'Title - {job}\n'
                    f'Link - {description[0]}\n'
                    f'Price - {description[1]}'
                )
                requests.get(
                    'https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_TOKEN),
                    params=dict(
                        chat_id=CHAT_ID,
                        text=text
                    ))
        current_data = now_data
        time.sleep(SLEEP_TIMER)


if __name__ == '__main__':
    main()
