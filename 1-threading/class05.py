from concurrent.futures import thread
import threading
import requests


def download_content(url):
    response = requests.get(url)
    print(f'Содержимое {url} имеет размер {len(response.text)} символов')
    print(response.elapsed)
    
    
urls = [
    "https://google.com/",
    "https://wargaming.net/",
    "https://microsoft.com"
]

threads = []

for url in urls:
    thread = threading.Thread(target=download_content, args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print('Все страницы скачаны!')
