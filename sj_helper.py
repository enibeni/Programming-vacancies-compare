import os
import requests
from itertools import count
from common import predict_rub_salary, get_average_salary


def fetch_vacancies_sj(keyword, town, period=30):
    token = os.getenv('SJ_TOKEN')
    vacancies = []
    total_found = 0
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': token
    }
    params = {
        'keyword': keyword,
        'town': town,
        'period': period,
    }

    for page in count():
        params.update({'page': page})
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        page_data = response.json()
        if not page_data['more']:
            break
        vacancies.extend(page_data['objects'])
        total_found = page_data['total']
    return vacancies, total_found


def get_predict_rub_salary_sj(vacancy):
    if vacancy['currency'] != 'rub':
        return None

    payment_from = vacancy['payment_from']
    payment_to = vacancy['payment_to']

    return predict_rub_salary(payment_from, payment_to)


def get_sj_statistics(languages):
    vacancies_info = {}
    for language in languages:
        vacancies, total_found = fetch_vacancies_sj(town='Moscow', keyword=language)
        salaries = [get_predict_rub_salary_sj(vacancy) for vacancy in vacancies]
        vacancies_info[language] = {}
        vacancies_info[language]['average_salary'] = get_average_salary(salaries)
        vacancies_info[language]['vacancies_found'] = total_found
        vacancies_info[language]['vacancies_processed'] = len(vacancies)
    return vacancies_info


