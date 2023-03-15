
symbols = ('@', '.', '!', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def user(email, password):
    return {
        'email': email,
        'password': password,
        'greeting': lambda email: print(f"Hello from {email}")
    }


def registration():
    return []


def validation(user, list):
    email, password, *args = user.values()
    global symbols
    for i in symbols[0:2]:
        if i not in email:
            rules_email = True
            break
        else:
            rules_email = False
    for j in symbols:
        if len(password) < 6:
            rules_password = True
            break
        elif j in password:
            rules_password = False
            break
        else:
            rules_password = True
    if rules_email or rules_password:
        raise TypeError("Invalid data")
    list.append(user)
    return True


registred = registration()

oleksii = user("oleksii@i.ua", "qwerty!")

is_valid = validation(oleksii, registred)

if is_valid:
    print(registred)
    for user in registred:
        print(user['email'])
