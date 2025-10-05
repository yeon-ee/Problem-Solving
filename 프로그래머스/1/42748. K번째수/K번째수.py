def solution(array, commands):
    answer = []
    for command in commands:
        cutted_array = array[command[0] - 1:command[1]]
        answer.append(sorted(cutted_array)[command[2] - 1])
    return answer