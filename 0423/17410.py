r, c, k = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(3)]

def solution(arr, method):
    new_arr, length = [],0 # 연산 후 반환 행렬 / 최대 길이 행 or 열
    for r in arr:
        num_cnt, new_r = [],[]
        for number in set(r):
            if number == 0:
                continue
            cnt = r.count(number)
            num_cnt.append((number,cnt))
        num_cnt = sorted(num_cnt, key = lambda x:[x[1],x[0]]) # 정렬
        for num, cnt in num_cnt:
            new_r += [num, cnt]
        new_arr.append(new_r)
        length = max(length, len(new_r))
    for r in new_arr:
        r += [0] * (length - len(r))
        if len(r) > 100 :
            r = r[:100]
    if method == 'C':
        return list(zip(*new_arr))
    else:
        return new_arr


answer = 0
while True:
    if answer > 100 :
        answer = -1
        break
    if 0 <= r-1 < len(arr) and 0 <= c-1 < len(arr[0]) and arr[r-1][c-1] == k :
        break
    if len(arr) >= len(arr[0]) : # 행의 개수 >= 열의 개수
        arr = solution(arr, 'R')
    else:
        arr = solution(list(zip(*arr)),'C')
    answer += 1
print(answer)