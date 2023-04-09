def solution(strings, n):
    strings.sort(key=lambda string: (string[n], string))
    return strings
