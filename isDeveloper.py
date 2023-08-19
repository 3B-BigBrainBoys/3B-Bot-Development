# Returns if user is a dev

from dotenv import load_dotenv
import os


def isDeveloper(id):
    load_dotenv()
    ids = [int(id) for id in os.getenv('DEV_IDS').split(',')]
    if id in ids:
        return True
    return False