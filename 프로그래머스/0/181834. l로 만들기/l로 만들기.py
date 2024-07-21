def solution(myString):
    result = ""
    for s in myString:
        if ord(s) < ord("l"):
            result += "l"
        else:
            result += s
    return result