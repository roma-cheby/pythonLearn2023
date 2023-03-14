import sys

def decrypt(line):
    parse = line.partition("..")
    if parse[1] == "..":
        return decrypt(parse[0][:-1] + parse[2])
    else:
        return line.replace('.','')

if __name__ == '__main__':
    line = sys.stdin.read()[:-1]
    print(decrypt(line))
