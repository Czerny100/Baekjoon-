def Ucleadean(a, b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

def solution(denum1, num1, denum2, num2):
    denum = denum1*num2 + denum2*num1
    num = num1*num2
    gcd = Ucleadean(denum, num)
    return [denum/gcd, num/gcd]