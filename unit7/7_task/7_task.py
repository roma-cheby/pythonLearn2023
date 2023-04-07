import logging
from dict_config import dict_config
import logging.config

def CreateLogger(name):
    logger = logging.getLogger(name)
    logging.config.dictConfig(dict_config)
    return logger

def Calculate():
    s = input("Знак (+,-,*,/): ")
    logger.info(f"Считан знак операции: {s}")
    if s in ('+', '-', '*', '/'):
        x = float(input("x = "))
        logger.info(f"Считано первое число: {x}")
        y = float(input("y = "))
        logger.info(f"Считано второе число: {y}")
        if s == '+':
            print("%.2f" % (x+y))
            logger.info("Выполнилось сложение чисел")
        elif s == '-':
            print("%.2f" % (x-y))
            logger.info("Выполнилось вычитание чисел")
        elif s == '*':
            print("%.2f" % (x*y))
            logger.info("Выполнилось умножение чисел")
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
                logger.info("Выполнилось деление чисел")
            else:
                logger.error("Ошибка - деление на 0!")
                print("Деление на ноль!")
    else:
        print("Этот знак не поддерживается данным калькулятором!")
        logger.error("Ошибка ввода знака действия")
        logger.info("ОШИБКА ASCII Ø∏‡°⁄·°")
    Calculate()

if __name__ == '__main__':
    logger = CreateLogger("Calculate")
    Calculate()