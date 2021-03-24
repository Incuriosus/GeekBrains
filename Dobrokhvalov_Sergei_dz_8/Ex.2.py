import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as logs:
    pattern = re.compile(r'((?:(?:(?:\d{1,3}\.){3})\d{1,3})|(?:(?:(?:\w{3,4}.){7})\w{4}))\s.+(\d{2}/\w{3}/'
                         r'(?:(?:\d{2,4}.){4})\+\d{4}).{3}(\w{3,4})\s((?:/.{9}){2}).+(\d{3})\s(\d+)')
    for log in logs:
        result_log = pattern.findall(log)
        print(result_log)
