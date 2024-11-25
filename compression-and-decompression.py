import re

def iter_solution(compressed_string):
    flag = True
    times = 0
    decompressed_text = ""
    seq = ""

    while flag:
        flag = False
        for c in compressed_string:
            if re.search(r"\d", c):
                times = times * 10 + int(c)
            
            elif re.search(r"\[", c):
                flag = True
            
            elif re.search(r"[a-zA-Z]", c):
                seq += c
            
            elif re.search(r"\]", c):
                decompressed_text += seq * times
                flag = False
                times = 0
                seq = ""

        if len(seq) > 0:
            decompressed_text += seq

        print(decompressed_text)
     

#iter_solution("10[a]")
#iter_solution("3[abc]4[ab]c")
iter_solution("2[3[a]b]")