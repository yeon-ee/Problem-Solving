def compare(A, B):
    if A == B:
        return True
    elif A[:len(B)] == B:
        return compare(A[len(B):], B)
    elif B[:len(A)] == A:
        return compare(A, B[len(A):])
    else:
        return A > B



def quick_sort(L):
    if len(L) > 1:
        pivot = L[0]
        left = []
        right = []
        for k in range(1, len(L)):
            if compare(L[k], pivot):
                right.append(L[k])
            else:
                left.append(L[k])
        return quick_sort(left) + [pivot] + quick_sort(right)
    return L

def solution(numbers):
    answer = ''
    string_numbers = [str(x) for x in numbers]
    sorted_string_numbers = quick_sort(string_numbers)
    for item in reversed(sorted_string_numbers):
        answer += item
    if answer[0] == '0':
        return '0'
    return answer