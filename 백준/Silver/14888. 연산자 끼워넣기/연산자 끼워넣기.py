from itertools import permutations

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        if a < 0 and b > 0:
            return ((a * (-1)) // b) * (-1)
        else:
            return a // b

M = -1000000000
m = 1000000000

N = int(input())
nums = list(map(int,input().split()))
ops_list = list(map(int,input().split()))
ops = ['+'] * ops_list[0] + ['-'] * ops_list[1] + ['*'] * ops_list[2] + ['/'] * ops_list[3]

ops_seqs = set(permutations(ops))
for ops_seq in ops_seqs:
    n = nums[0]
    for i in range(N - 1):
        op = ops_seq[i]
        n = calculate(n, nums[i + 1], op)
    M = max(n, M)
    m = min(n, m)
print(M)
print(m)