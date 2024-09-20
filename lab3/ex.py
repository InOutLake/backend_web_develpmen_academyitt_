from datetime import datetime
def get_age():
    birth_year = int(input('Введите год рождения: '))
    current_year = datetime.now().year
    age = current_year - birth_year
    years_to_retire = 65 - age
    print('Ваш возраст:', age)
    if years_to_retire > 0:
        print('До пенсии вам осталось:', years_to_retire, 'лет')
    else:
        print('Вы успешно дожили до пенсии, поздравляем!')

def get_user_info():
    name = input('Введите фамилию, имя и отчество: ')
    name_list = name.split()
    print('Фамилия: {}\nИмя: {}\nОтчество: {}'.format(*name_list))

def get_subjects():
    subjects = ['Математика', 'Физика', 'Химия', 'Биология', 'География', 'История']
    for i, subject in enumerate(subjects, 1):
        print(i, subject, sep=': ')
    print('Введите номера предметов, которые вам не нравятся (через пробел):')
    bad_subjects = list(map(int, input().split()))
    for subject in bad_subjects:
        del subjects[subject - 1]
    print('Остались:', ', '.join(subjects))

if __name__ == '__main__':
    get_user_info()
    get_age()
    get_subjects()
