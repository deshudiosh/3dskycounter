import json
from collections import Counter
from statistics import mean


def analize_dump(dump_name):
    with open(dump_name, 'r') as f:
        data = json.load(f)

    pro_downloads = [item['downloads'] for item in data if item['is_pro']]
    num_pro_downloads = sum(pro_downloads)
    avg_pro_downloads = round(mean(pro_downloads))
    print(num_pro_downloads)

    free_downloads = [item['downloads'] for item in data if not item['is_pro']]
    num_free_downloads = sum(free_downloads)
    # print(num_free_downloads)
    return num_pro_downloads

if __name__ == '__main__':
    sales1 = analize_dump("dumps/deckorator_2019-08-27_18-29-18.json")
    sales2 = analize_dump("dumps/deckorator_2019-08-28_18-27-04.json")
    earned = (sales2-sales1) * 7 * .7 * 3.93
    print(earned)
