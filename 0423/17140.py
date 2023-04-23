r, c, k = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(3)]

def solution(arr, method):
    new_arr, length = [],0 # 연산 후 반환 행렬 / 최대 길이 행 or 열
    for r in arr:
        # 각 숫자의 빈도와 함께 저장하는 num_cnt, 연산 결과를 저장하는 리스트 new_r
        num_cnt, new_r = [],[]

        # 각 숫자에 대해서 빈도를 세어 num_cnt에 할당
        for number in set(r):
            if number == 0:
                continue

            cnt = r.count(number)
            num_cnt.append((number,cnt))

        # 빈도를 기준으로 오름차순 정렬. 빈도가 같은 경우에는 숫자를 기준으로 오름차순 정렬
        num_cnt = sorted(num_cnt, key = lambda x:[x[1],x[0]]) 
        for num, cnt in num_cnt:
            new_r += [num, cnt]
        new_arr.append(new_r)
        
        # length를 최대 길이인 행 또는 열의 길이로 업데이트
        length = max(length, len(new_r))

    # 모든 행에 대한 연산을 마친 후, 각 행의 길이를 최대 길이인 행 또는 열의 길이와 같아지도록 0으로 채움
    for r in new_arr:
        r += [0] * (length - len(r))
        if len(r) > 100 :
            r = r[:100]

    # method가 'C'인 경우에는 new_arr을 전치하여 반환하고, 그렇지 않은 경우에는 new_arr을 반환
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