def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # 각 요소의 기본 길이는 1
    
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:  # 앞의 요소보다 현재 요소가 크다면
                dp[i] = max(dp[i], dp[j] + 1)  # 더 긴 수열 선택
    
    return max(dp)  # 최댓값이 최종 길이

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# 결과 출력
print(longest_increasing_subsequence(arr))
