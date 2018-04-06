from requests_html import HTMLSession
import sys


def display_result():
    url = 'http://ketqua.net/'

    session = HTMLSession()
    resp = session.get(url)
    if resp.status_code == 200:
        table = resp.html.find('table', first=True)
        print(table.text)


def get_result():
    result = None
    url = 'http://ketqua.net/'

    session = HTMLSession()
    resp = session.get(url)
    if resp.status_code == 200:
        table = resp.html.xpath('//table/tbody')
        loto = table[1].text
        result = loto.split('\n')
    else:
        print('Chịu thua. get.status_code ='.format(resp.status_code))
    return result


def check_result(number):
    if number not in get_result():
        return 0
    else:
        count = get_result().count(number)
        return count


def main():
    numbers = sys.argv[1:]

    if len(numbers) == 0:
        display_result()

    for number in numbers:
        if check_result(number[-2:]) == 0:
            print('Đen thôi đỏ quên đi! Đã bảo đừng đánh con này rồi mà -_-')
        elif check_result(number[-2]) == 1:
            print('Hay lắm được 1 nháy con {} rồi. Đi nhậu thôi'
                  .format(number[-2:]))
        else:
            print('Wtf trúng tận {} nháy con {} cơ à. Híc, lộc ae tí đi!'
                  .format(check_result(number[-2:]), number[-2:]))


if __name__ == "__main__":
    main()
