import urllib.request
import re
import datetime


def get_number():
    with open("README.md", 'r', encoding="utf8") as f:
        last_line = f.readlines()[-1]
    number = int(last_line[:3]) + 1
    if number < 10:
        s_number = '00' + str(number)
    elif number < 100:
        s_number = '0' + str(number)
    else:
        s_number = str(number)
    return s_number


def get_title(num):
    url = "https://www.acmicpc.net/problem/" + num
    html = urllib.request.urlopen(url)
    html_contents = str(html.read().decode("UTF-8"))

    results = re.findall("(\<span id=\"problem_title\"\>)([\s\S]+?)(\<\/span\>)", html_contents)
    t = results[0][1]
    return t


def get_date():
    now = datetime.datetime.now()
    if now.month < 10:
        month = '0' + str(now.month)
    else:
        month = str(now.month)
    if now.day < 10:
        day = '0' + str(now.day)
    else:
        day = str(now.day)
    d = str(now.year) + '/' + month + '/' + day
    return d


def set_purl(pnum):
    purl = "https://www.acmicpc.net/problem/" + pnum
    return purl


def set_surl(date, snum):
    surl = "https://github.com/july5amp/algorithm-study/tree/master/" + date[:4] + '/' + snum
    return surl


def file_write(number, date, num, title, purl, surl):
    line = number + " | " + date + " | [백준 " + num + ' - ' + title + "](" + purl + ") | [답안](" + surl + ")\n"
    with open("README.md", 'a', encoding="utf8") as f:
        f.write(line)


def main():
    number = get_number()
    num = input("백준 문제 번호 입력: ")
    title = get_title(num)
    date = get_date()
    purl = set_purl(num)
    surl = set_surl(date, number)
    file_write(number, date, num, title, purl, surl)


if __name__ == '__main__':
    main()