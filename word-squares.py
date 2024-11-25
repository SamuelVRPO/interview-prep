def check_word_square(words: list[str]) -> bool:
    for i, _ in enumerate(words):
        for j, _ in enumerate(words[i]):
            if words[i][j] != words[j][i]:
                return False
    
    return True


def find_word_squares(words: list[str]):
    word_squares = []
    for i, _ in enumerate(words):
        remaining_words = words[:]
        square = []
        square.append(words[i])
        remaining_words.remove(words[i])
        for j in range(1, len(words[i])):
            for k in range(j):
                for word in remaining_words:



result = check_word_square(['BALL', 'AREA', 'LEAD', 'LADY'])
print(find_word_squares(['AREA', 'BALL', 'DEAR', 'LADY', 'LEAD', 'YARD']))