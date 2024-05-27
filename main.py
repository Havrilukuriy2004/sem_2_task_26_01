import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_web_time(url):
    response = requests.get(url)
    response.raise_for_status()  # Перевірка на успішність запиту

    soup = BeautifulSoup(response.text, 'html.parser')
    time_span = soup.find('span', {'id': 'ct'})

    if time_span:
        web_time_str = time_span.text.strip()
        web_time = datetime.strptime(web_time_str, '%H:%M:%S')
        return web_time
    else:
        raise ValueError('Time span with id "ct" not found.')

def compare_time(web_time):
    local_time = datetime.now().time()
    print(f"Local Time: {local_time.strftime('%H:%M:%S')}")
    print(f"Web Time: {web_time.strftime('%H:%M:%S')}")

    if local_time.hour == web_time.hour and local_time.minute == web_time.minute and abs(local_time.second - web_time.second) < 5:
        print("Local time is synchronized with web time.")
    else:
        print("Local time is not synchronized with web time.")

if __name__ == '__main__':
    url = 'https://www.timeanddate.com/worldclock/ukraine/kyiv'
    try:
        web_time = get_web_time(url)
        compare_time(web_time)
    except Exception as e:
        print(f"Error: {e}")
