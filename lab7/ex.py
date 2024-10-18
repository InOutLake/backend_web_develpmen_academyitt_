from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    position: str
    hobbies: list[str]
    specialization: str
    experience: int

def assign_user_info():
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    position = input("Введите должность: ")
    hobbies = input("Введите хобби (через запятую): ").split(',')
    hobbies = [hobby.strip() for hobby in hobbies]
    specialization = input("Введите направление деятельности: ")
    experience = int(input("Введите стаж работы: "))

    user = User(
        name=name,
        age=age,
        position=position,
        hobbies=hobbies,
        specialization=specialization,
        experience=experience
    )
    return user

def main():
    user = assign_user_info()
    json_data = user.model_dump_json(indent=4)
    with open('lab7/user_info.json', 'w', encoding='utf-8') as f:
        f.write(json_data)

if __name__ == "__main__":
    main()
    