def solution(my_string):
    answer = ""
    el = set(my_string)
    for let in my_string:
        if let in el:
            answer += let
            el.discard(let)
    return answer
