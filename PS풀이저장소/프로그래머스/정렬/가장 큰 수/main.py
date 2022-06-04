def solution(numbers):
    answer = ''
    numbers_strings = [str(x) for x in numbers]
    numbers_strings.sort(key = lambda x : x*3, reverse = True)
    if numbers_strings[0] == '0':
        return '0'
    return ''.join(numbers_strings)