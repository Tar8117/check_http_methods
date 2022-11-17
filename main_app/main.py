import json
from time import sleep

import requests
import validators

method_list = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'PATCH', 'TRACE']


def check_available_methods(string):
    data = {}
    res_dict = {}
    for i in string:
        valid = validators.url(i)
        if not valid:
            print(f'Строка "{i}" не является ссылкой')
        else:
            print(f'Строка "{i}" является ссылкой. Начинаю проверку доступных http методов...')
            sleep(2)
            for method in method_list:
                req = requests.request(method, i)
                if req.status_code != 405:
                    res_dict[method] = req.status_code
            data[i] = res_dict
            json_formatted_str = json.dumps(data, indent=3)
            return json_formatted_str


def main():
    n = int(input('Введите количество строк: '))
    s = [input('Введите строку: ') for _ in range(n)]
    print(check_available_methods(s))


if __name__ == '__main__':
    main()
