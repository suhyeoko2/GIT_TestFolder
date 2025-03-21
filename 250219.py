# 리스트의 합을 계산하는 함수
def calculate_sum(numbers):
    """ 주어진 숫자 리스트의 합을 반환하는 함수 """
    total = 0
    for num in numbers:
        total += num
    return total


# 평균을 계산하는 함수 (버그 포함)
def calculate_average(numbers):
    """ 주어진 숫자 리스트의 평균을 반환하는 함수 """
    total = calculate_sum(numbers)
    count = len(numbers)
    return total / count  # count가 0일 때 에러 발생 가능!


# 메인 실행 코드
if __name__ == "__main__":
    num_list = [10, 20, 30, 40, 50]
    print("리스트의 합:", calculate_sum(num_list))

    empty_list = []
    print("빈 리스트의 평균:", calculate_average(empty_list))  # 여기서 오류 발생 가능
