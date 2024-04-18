from verification import PasswordChecker
from settings import requirements


def register_user(username=None):
    if username is None:
        print("Регистрация нового пользователя")
        username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    password_checker = PasswordChecker(password, requirements)
    failed = password_checker.is_valid()

    if not failed:
        print("Пароль корректен. Пользователь", username, "зарегистрирован.")
    else:
        print("Пароль не соответствует требованиям. Повторите регистрацию.")
        for requirement in failed:
            print(requirement)
        register_user(username)


register_user()
