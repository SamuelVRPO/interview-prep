import re

def solution(word: str) -> int:
    unique_chars = {}
    num_special_chars = 0

    for char in word:
        if unique_chars.get(char) == None:
            unique_chars[char] = 1
    
    for char in unique_chars:
        if unique_chars.get(char) != None and re.search(r"[a-z]", char):
            if unique_chars.get(char.upper()):
                num_special_chars += 1

    print(num_special_chars)

solution("abBcab")