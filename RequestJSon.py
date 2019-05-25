import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    print(resp)
    data_model = json.loads(resp.text)

    for news in data_model['newslist']:
        print(news['title'])

main()
