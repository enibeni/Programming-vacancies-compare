from dotenv import load_dotenv
from common import print_statistics_in_table_view
from hh_helper import get_hh_statistics
from sj_helper import get_sj_statistics

LANGUAGES = ['Python', 'Java', 'JavaScript', 'C#', 'Elixir', 'Ruby', 'Go', 'Scala']


if __name__ == '__main__':
    load_dotenv()
    print(f'Загружаем вакансии для языков {", ".join(LANGUAGES)}')
    hh_vacancies = get_hh_statistics(LANGUAGES)
    sj_vacancies = get_sj_statistics(LANGUAGES)

    print_statistics_in_table_view('HeadHunter Moscow', hh_vacancies)
    print_statistics_in_table_view('SuperJob Moscow', sj_vacancies)




