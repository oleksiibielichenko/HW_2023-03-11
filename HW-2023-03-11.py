
def person(email, password):
    return {
        'email': email,
        'password': password,
        'greeting': lambda email: print(f"Hello from {email}")
    }


def registration():
    return []


symbols = ('@', '.', '!', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

for


def validation(person, arr):
    email, password, *args = person.values()
    rules_email =
    not in email,
        '.' not in email,
    }
    rules_password = len(password) < 6 or password.find('!') == -1
    if rules_email or rules_password:
        raise TypeError("Invalid data")
    arr.append(person)
    return True


registred = registration()

oleksii = person("oleksii@i.ua", "123!987")

oleksii['greeting'](oleksii['email'])
