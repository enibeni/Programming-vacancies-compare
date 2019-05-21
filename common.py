from terminaltables import AsciiTable


def get_average_salary(salaries):
    salaries = [salary for salary in salaries if salary is not None and salary != 0]
    if salaries is None or salaries == []:
        return None
    average_salary = int(sum(salaries) / len(salaries))
    return average_salary


def predict_rub_salary(salary_from, salary_to):
    if not salary_from or salary_to:
        return None
    if salary_from and salary_to:
        return (int(salary_from) + int(salary_to)) / 2
    elif salary_from:
        return int(salary_from) * 1.2
    elif salary_to:
        return int(salary_to) * 0.8


def print_statistics_in_table_view(table_title, data):
    title = table_title
    table_data = []
    table_column_names = ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']
    table_data.append(table_column_names)
    for language, language_data in data.items():
        table_data.append(
            [
                language,
                language_data['vacancies_found'],
                language_data['vacancies_processed'],
                language_data['average_salary']
            ]
        )
    table_instance = AsciiTable(table_data, title)
    print(table_instance.table)
