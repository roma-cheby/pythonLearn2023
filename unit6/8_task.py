wordlist = [line.strip() for line in open('words.txt')]

dict_numbers_and_letters = {'2': ["a", "b", "c"],
                            "3" : ["d", "e", "f"],
                            "4" : ["g", "h", "i"],
                            "5" : ["j", "k", "l"],
                            "6" : ["m", "n", "o"],
                            "7" : ["p", "q", "r", "s"],
                            "8" : ["t", "u", "v"],
                            "9" : ["w", "x", "y", "z"]}

def my_t9(code):
    l = len(code)
    work_wordlist = [x for x in wordlist if len(x) == l]
    for i in range(l):
        letters = dict_numbers_and_letters[code[i]]
        work_wordlist = [x for x in work_wordlist if x[i] in letters]
    return work_wordlist

print(my_t9(input()))