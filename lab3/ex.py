from datetime import datetime
def get_age_scenario():
    birth_year = int(input('Введите год рождения: '))
    current_year = datetime.now().year
    age = current_year - birth_year
    years_to_retire = 65 - age
    print('Ваш возраст:', age)
    if years_to_retire > 0:
        print('До пенсии вам осталось:', years_to_retire, 'лет')
    else:
        print('Вы успешно дожили до пенсии, поздравляем!')

def get_user_info_scenario():
    name = input('Введите фамилию, имя и отчество: ')
    name_list = name.split()
    print('Фамилия: {}\nИмя: {}\nОтчество: {}'.format(*name_list))

def delete_bad_subjects_scenario():
    subjects = ['Математика', 'Физика', 'Химия', 'Биология', 'География', 'История']
    for i, subject in enumerate(subjects, 1):
        print(i, subject, sep=': ')
    print('Введите номера предметов, которые вам не нравятся (через пробел):')
    bad_subjects = list(map(int, input().split()))
    subjects = [subject for i, subject in enumerate(subjects) if i+1 not in bad_subjects]
    print('Остались:', ', '.join(subjects))

if __name__ == '__main__':
    get_user_info_scenario()
    get_age_scenario()
    delete_bad_subjects_scenario()
