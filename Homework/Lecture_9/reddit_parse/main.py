#!/usr/bin/python3

import requests
import time
import re

def get_me_some_reddit(url, headers):

    current_date_time = time.ctime()
    r = requests.get(url, headers)

    if r.status_code == 200:
        with open('./reddit.txt', 'w') as file:
            file.write('\n\n' + current_date_time + '\n\n')
            file.write(r.text)
            return True

    return False

def extractComments():
    comments = {}
    pattern = r'(?:(data-author=\")([^\"]+)(.+)(\"md\"><p>)(.+)(</p>))'

    with open('./reddit.txt') as file:
        for line in file:
            found = re.search(pattern, line)
            if found:
                author = found.group(2)
                comment = found.group(5)
                if author not in comments.keys():
                    comments[author] = [comment]
                else:
                    comments[author].append(comment)

    return comments

if __name__ == '__main__':

    url = 'https://www.reddit.com/r/Python/\
comments/806my0/requestshtml_html_parsing_for_humans/'

    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}


    fetched_data = get_me_some_reddit(url, headers)

    if fetched_data:
        extracted_comments = extractComments()
        for k, v in extracted_comments.items():
            print()
            print('-' * 30)
            print(k + ':')
            for comment in v:
                print()
                print(comment)
    else:
        print('Reddit is being suspicious or the resource is down (unlikely:)')

