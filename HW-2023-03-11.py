
symbols = ('@', '.', '!', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def person(email, password):
    return {
        'email': email,
        'password': password,
        'greeting': lambda email: print(f"Hello from {email}")
    }


def registration():
    return []


def validation(person, list):
    email, password, *args = person.values()
    global symbols
    for i in symbols[0:2]:
        if i not in email:
            rules_email = True
        else:
            rules_email = False
    for j in symbols:
        if len(password) < 6:
            rules_password = True
        if j not in password:
            rules_password = True
        else:
            rules_password = False
    if rules_email or rules_password:
        raise TypeError("Invalid data")
    list.append(person)
    return True


registred = registration()

oleksii = person("oleksiii.ua", "01234569")

is_valid = validation(oleksii, registred)

if is_valid:
    print(registred)
    print('________')
    for person in registred:
        print(person['email'])

oleksii['greeting'](oleksii['email'])
