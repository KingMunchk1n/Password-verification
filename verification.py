import re


class PasswordChecker:
    def __init__(self, password, requirements):
        self.password = password
        self.requirements = requirements

    def is_valid(self):
        failed = []
        for key, value in self.requirements.items():
            if key == "length" and len(self.password) < value:
                failed.append(f"Длина пароля должна быть не менее {value} символов")
            if key == "digits" and not bool(re.search(r"\d", self.password)):
                failed.append("Пароль должен содержать цифры")
            if key == "lower" and not bool(re.search(r"[a-z]", self.password)):
                failed.append("Пароль должен содержать строчные буквы")
            if key == "upper" and not bool(re.search(r"[A-Z]", self.password)):
                failed.append("Пароль должен содержать заглавные буквы")
            if key == "char" and not bool(re.search(r"[~!@#$%^&*+-/.,\\{}[\]();:<>\"'_]", self.password)):
                failed.append("Пароль должен содержать специальные символы")
        return failed
