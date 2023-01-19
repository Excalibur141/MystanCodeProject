"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    start = time.time()
    ####################
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        word = str(input("Find anagrams for:"))
        if word == EXIT:
            break
        else:
            print("Searching...")
            find_anagrams(word)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():  # read file and return to list
    dictionary_list = []
    with open(FILE, 'r') as f:
        for line in f:
            dictionary = line.split()
            for token in dictionary:
                ans = ""
                for ch in token:
                    if ch.isalpha():
                        ans += ch
                dictionary_list.append(ans)
    return dictionary_list


def simple_dictionary(s, dictionary_list):  # delete 1. strings of different lengths 2. strings of different characters
    """
    :param s: str
    :param dictionary_list: list
    :return: list
    """
    simple_list = []
    for token in dictionary_list:
        if len(s) == len(token):  # delete strings of different lengths
            if sorted(s) == sorted(token):  # delete strings of different characters
                simple_list.append(token)
    return simple_list


def find_anagrams(s):
    """
    :param s: str
    :return: list
    """
    ans_list = []
    simple_list = simple_dictionary(s, read_dictionary())
    find_anagrams_helper(s, "", ans_list, simple_list)
    print(len(ans_list), "anagrams:", ans_list)


def find_anagrams_helper(s, anagram_s, ans_list, simple_list):
    """
    :param s: str
    :param anagram_s: str
    :param ans_list: list
    :param simple_list: list
    :return: list
    """
    if len(anagram_s) == len(s):  # strings of the same length
        if sorted(anagram_s) == sorted(s):  # string exists in the dictionary
            if anagram_s not in ans_list:  # remove duplicate count
                print("Found:", anagram_s)
                print("Searching...")
                ans_list.append(anagram_s)
    else:
        for alphabet in s:
            if has_prefix(anagram_s, simple_list) is not True:  # early stopping
                pass
            else:
                # Choose
                anagram_s += str(alphabet)
                # print("anagram_s:", anagram_s)  # only for test
                # Explore
                find_anagrams_helper(s, anagram_s, ans_list, simple_list)
                # Un-choose
                anagram_s = anagram_s[:-1]


def has_prefix(sub_s, simple_list):
    """
    :param sub_s: str
    :param simple_list: list
    :return: boolean
    """
    count = 0
    for token in simple_list:
        if token.startswith(sub_s):
            count += 1
    if count == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    main()
