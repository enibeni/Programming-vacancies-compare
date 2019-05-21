import requests
from itertools import count
from common import predict_rub_salary, get_average_salary


def fetch_vacancies_hh(text=None, area=None, period=30):
    vacancies = []
    total_found = 0
    url = 'https://api.hh.ru/vacancies'
    headers = {
        'User-Agent': 'DevmanApp/1.0 (se.mrzv@gmail.com)'
    }
    params = {
        'text': text,
        'area': area,
        'period': period,
        'per_page': 100
    }

    for page in count():
        params.update({'page': page})
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        page_data = response.json()
        if page >= page_data['pages'] - 1:
            break
        vacancies.extend(page_data['items'])
        total_found = page_data['found']
    return vacancies, total_found


def get_predict_rub_salary_hh(vacancy):
    salary_data = vacancy['salary']

    if not salary_data:
        return None

    if salary_data['currency'] != 'RUR':
        return None

    salary_from = salary_data['from']
    salary_to = salary_data['to']

    return predict_rub_salary(salary_from, salary_to)


def get_hh_statistics(languages):
    area_code_for_moscow = 1
    vacancies_info = {}
    for language in languages:
        vacancies, total_found = fetch_vacancies_hh(
            text=language,
            area=area_code_for_moscow
        )
        salaries = [get_predict_rub_salary_hh(vacancy) for vacancy in vacancies]
        vacancies_info[language] = {}
        vacancies_info[language]['vacancies_found'] = total_found
        vacancies_info[language]['vacancies_processed'] = len(vacancies)
        vacancies_info[language]['average_salary'] = get_average_salary(salaries)
    return vacancies_info
