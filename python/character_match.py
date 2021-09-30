# reference https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/

from collections import Counter


def is_character_match(string1, string2):
    # implementing counter function
    if Counter(string1.lower().replace(" ", "")) == Counter(string2.lower().replace(" ", "")):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


is_character_match("Anna Madrigal", "A man and a girl")
