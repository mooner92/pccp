def solution(s):
    answer = ""
    letdict = {}
    exl = []
    for letter in s:
        if letdict.get(letter, -1) == -1:
            letdict[letter] = 1
        else:
            letdict[letter] += 1
    for key, val in letdict.items():
        if val == 1:
            exl.append(key)
    exl.sort()
    answer = "".join(exl)
    return answer
