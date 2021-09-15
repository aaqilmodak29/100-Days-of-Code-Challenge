def isValid(password):
    if len(password) < 8 or len(password) > 15:
        return False

    if " " in password:
        return False

    if True:
        count = 0

        arr = ['0', '1', '2', '3',
               '4', '5', '6', '7', '8', '9']

        for i in password:
            if i in arr:
                count = 1
                break

        if count == 0:
            return False

    if True:
        count = 0

        arr = ['@', '#', '!', '~', '$', '%', '^',
               '&', '*', '(', ',', '-', '+', '/',
               ':', '.', ',', '<', '>', '?', '|']

        for i in password:
            if i in arr:
                count = 1
                break
        if count == 0:
            return False

    if True:
        count = 0

        for i in range(65, 91):

            if chr(i) in password:
                count = 1

        if count == 0:
            return False

    if True:
        count = 0

        for i in range(90, 123):

            if chr(i) in password:
                count = 1

        if count == 0:
            return False

    return True


password1 = input('Please enter the password: ')

if isValid([i for i in password1]):
    print("Valid Password")
else:
    print("Password invalid/Please enter a stronger password!")
