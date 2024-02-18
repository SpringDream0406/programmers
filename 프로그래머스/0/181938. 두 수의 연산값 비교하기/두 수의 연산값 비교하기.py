def solution(a, b):
    answer = int(f"{a}{b}" if int(f"{a}{b}") >= 2*a*b else f"{2*a*b}")
    return answer