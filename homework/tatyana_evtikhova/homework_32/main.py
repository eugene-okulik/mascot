import requests
import time


def check_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Сайт {url} доступен')
    else:
        print(f'Сайт {url} недоступен. Статус код: {response.status_code}')


def main():
    url = "https://www.onliner.by/"
    check_interval = 20
    while True:
        check_website(url)
        time.sleep(check_interval)


if __name__ == "__main__":
    main()
