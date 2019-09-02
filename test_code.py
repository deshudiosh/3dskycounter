import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()

data = []

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        l = len(response.content)
        print(f"Read {l} from {url}")
        data.append(l)


if __name__ == "__main__":

    username = "deckorator"

    sites = []
    for i in range(10):
        sites.append("https://3dsky.org/users/{}/models?page={}".format(username, i))

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_site, sites)

    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
    print(data)