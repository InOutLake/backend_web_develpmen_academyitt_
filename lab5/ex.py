import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lab3.ex import delete_bad_subjects_scenario
def sports_scenario():
    sports = ['хоккей', 'футбол']
    print("Виды спорта: {}".format(', '.join(sports)))
    new_sport = input('Какой ваш любимый вид спорта?\nВведите его: ')
    sports.append(new_sport)
    # using set in case of duplicates
    sports = sorted(list(set(sports)))
    print("Виды спорта: {}".format(', '.join(sports)))

if __name__ == '__main__':
    sports_scenario()
    delete_bad_subjects_scenario()
    
