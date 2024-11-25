def find_substring(word, S):
    idx = 0
    new_S = S[:]
    for i, w in enumerate(word):
        found = False
        for j, s in enumerate(new_S):
            if new_S[j] == word[i]:
                found = True
                new_S = new_S[j+1:]
                break
        
        if not found:
            return False
    
    return True

def solution(S, D):
    longest_word = ""
    for word in D:
        found = find_substring(word, S)
        if found and len(word) > len(longest_word):
            longest_word = word
        
    print(longest_word)


S = "abppplee"
D = {
    "able",
    "ale",
    "apple",
    "bale",
    "kangaroo",
}

solution(S, D)