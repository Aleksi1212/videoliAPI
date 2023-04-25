import random, string

def generateRandomString(length: int):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))