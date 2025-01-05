N = int(input())

nums = list(map(int, input().split()))
nums.sort()

answer_list = nums[:N // 2 + N % 2] + nums[N // 2 + N % 2:][::-1]
answer = abs(answer_list[N - 1] - answer_list[0])

for i in range(1, N):
    answer += abs(answer_list[i] - answer_list[i - 1])
    
print(answer)
