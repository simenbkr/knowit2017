from collections import Counter
from itertools import permutations, repeat

def isPal(word):
    return word == word[::-1]

def get_palindromes(word):
    word = word.lower()
    char_counts = Counter(word)
    num_odd_counts = sum(int(c % 2 != 0) for c in char_counts.values())
    if num_odd_counts > 1:
        return []
    odd_char = '' if num_odd_counts == 0 else [char for char, count in char_counts.items() if count % 2 == 1][0]
    even_chars = [rep_char for char, count in char_counts.items()
                  for rep_char in repeat(char, count / 2) if count % 2 == 0]
    return [perm_word + odd_char + perm_word[::-1]
            for perm_word in set(
                    ''.join(char_perm)
                    for char_perm in permutations(even_chars))]


def main():
    count = 0
    for line in lista:
        if isPal(line):
            continue
        pals = get_palindromes(line)
        if len(pals) > 0:
            count += 1

    print count

if __name__ == '__main__':
    with open('ordbok.txt','r') as f:
        lista = [x.strip().strip('\n') for x in f.readlines()]
        f.close()
    main()
