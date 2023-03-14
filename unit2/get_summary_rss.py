def get_summary_rss(path):
    lines = open(path).readlines()[1:]
    summary_rss = 0
    for line in lines:
        summary_rss += int(line.split()[5])
    return f"Суммарный вес {summary_rss // (2**20)} мегабайт {(summary_rss % (2**20)) // 2**10} килобайт {summary_rss % 2**10} байт"

if __name__ == '__main__':
    file_name = "output_file.txt"
    print(get_summary_rss(file_name))


