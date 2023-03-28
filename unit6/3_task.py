# -*- coding: utf8 -*-
import getpass
import hashlib
import json
import logging

class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        msg = json.dumps(msg, ensure_ascii=False).encode('utf8').decode()
        return msg, kwargs

logger = JsonAdapter(logging.getLogger("password_checker"))

wordlist = [line.strip() for line in open('words.txt')]
wordlist = [x.lower() for x in wordlist if len(x) > 4]
def is_strong_password(password):
    return password.upper() in wordlist

def input_and_check_password():
    logger.debug("Начало input_and_check_password")
    password = getpass.getpass()
    is_strong_password(password)
    if not password:
        logger.warning("Вы ввели пустой пароль")
        return False

    try:
        hasher = hashlib.md5()
        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == "098f8":
            return True

    except ValueError as ex:
        logger.error("Вы ввели некорректный символ", exc_info=ex)

    return False

if __name__ == "__main__":

    logging.basicConfig(datefmt="%H:%M:%S",
                        format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}',
                        filename="skillbox_json_messages.log",
                        level=logging.INFO)
    logger.info("Вы пытаетесь аутентифицироваться в SkillBox")
    count_number = 3
    logger.info(f"У вас есть {count_number} попыток")
    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1
    logger.error("Пользователь трижды ввёл неправильный пароль!")
    exit(1)