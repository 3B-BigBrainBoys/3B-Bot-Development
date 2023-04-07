# Returns if user is a dev

from dotenv import load_dotenv


def isDeveloper(id):
    load_dotenv()
    if id in [261662217424994306, 270711617686208513, 252514565001052160]:
        return True
    return False