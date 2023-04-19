import random, string

def generateRandomString(length: int):
    characters = f'{string.ascii_letters}1234567890'

    id = ''.join([random.choice(characters) for i in range(length)])
    return id