# 투포인터
def solution(sequence, k):
    start, end = 0, 0
    value = sequence[start]
    min_length = 987654321
    answer = []

    while start < len(sequence) and end < len(sequence):
        if value < k:
            if end + 1 < len(sequence):
                end += 1
                value += sequence[end]
            else:
                break  # 배열의 끝에 도달하면 반복문을 종료합니다.
        elif value > k:
            value -= sequence[start]
            start += 1
        else:
            length = end - start
            if length < min_length:
                min_length = length
                answer = [start, end]
            value -= sequence[start]
            start += 1

    return answer