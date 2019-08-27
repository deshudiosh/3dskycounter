import datetime
import json

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


def scrape_user():
    username = "deckorator"

    data = []

    i = 0
    page_has_items = True
    while page_has_items:
        i += 1
        url = "https://3dsky.org/users/{}/models?page={}".format(username, i)
        result = requests.get(url)
        c = result.content
        soup = BeautifulSoup(c, features="html.parser")
        items = soup.find_all("div", "item")

        if len(items) > 0:
            for item in items:  # type: Tag
                is_pro = item.get_text().split()[0].find("pro") > -1
                downloads = int(item.find('a', 'icon_enter').get_text(strip=True))
                comments = int(item.find('a', 'icon_views').get_text(strip=True))
                likes = int(item.find('a', 'icon_reiting').get_text(strip=True))
                name = " ".join(item.contents[0].get('rel'))
                link = item.contents[0].get('href')

                obj = {"link": link, "name": name, "is_pro": is_pro, "downloads": downloads, "comments": comments, "likes": likes}
                data.append(obj)

            print("Page number {} scraped".format(i))
        else:
            page_has_items = False

    filename = "dumps/{}_{}.json".format(username, datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    with open(filename, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    scrape_user()

