import sys
import requests
import logging
import json
logger = logging.getLogger(__name__)


def get_result(key):
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='
    'coffee&location=10.779614,106.699256&radius=5000&key={}'
    data, results = None, [], []

    resp = requests.get(url.format(key)).json()
    for _ in range(3):
        data.append(resp)
        url = url + '&next_page_token=' + resp['next_page_token']
        logger.debug('%s is: ', url)
    for page in data:
        for coffee in page['results']:
            if len(results) < 50:
                results.append({'name': coffee['name'], 'address':
                                coffee['formatted_address']})

    return results


def main():
    agrument = sys.argv[1:]
    if len(agrument) > 1:
        print('python3 coffee_hcm.py your_token')
        sys.exit(2)
    with open('hcm_coffee.json', 'w') as file:
        json.dump(get_result(agrument[0]), file)


if __name__ == "__main__":
    main()

