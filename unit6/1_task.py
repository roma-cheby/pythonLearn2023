import getpass
import hashlib
import logging

logger = logging.getLogger("password_checker")

def input_and_check_password():
    logger.debug("Начало input_and_check_password")
    password = getpass.getpass()

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
                        format=f'%(asctime)s %(levelname)s %(message)s',
                        filename="stderr.txt",
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