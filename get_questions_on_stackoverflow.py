import sys
import requests


def get_question(N, tag):

    url = ('https://api.stackexchange.com/2.2/questions?pagesize='
           '{}&order=desc&sort=votes&tagged={}&site=stackoverflow')

    resp = requests.get(url.format(N, tag))
    data = resp.json()
    questions = data['items']
    return questions


def foo(questions):
    result = []
    for question in questions:
        result.append({'title': question['title'],
                       'link': question['owner']['link']})
    return result


def main():
    try:
        argument = sys.argv[1:]
        for question in foo(get_question(argument[0], argument[1])):
            print(question['title'] + '\n' + question['link'])
    except IndexError:
        print('python3 ex9_3.py N tag')


if __name__ == '__main__':
    main()
