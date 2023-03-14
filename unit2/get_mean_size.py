import sys

def get_mean_size(lines):
    summary = 0
    for line in lines:
        summary += int(line.split()[4])
    mean_size = summary // len(lines)
    return f"Средний вес файлов в папке {mean_size // (2 ** 20)} мегабайт {(mean_size % (2 ** 20)) // 2 ** 10} килобайт {mean_size % 2 ** 10} байт"

if __name__ == '__main__':
    lines = sys.stdin.readlines()[1:]
    print(get_mean_size(lines))