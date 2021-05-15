import sys
input = sys.stdin.readline
N = input()

#한줄 단위로 입력받는다. 때문에 개행문자 같이 입력됨.
#변수 타입이 문자열 형태로 저장되기 때문에 형변환 요구됨.

num_list = list(map(int, input().split()))
#map은 반복 가능한 객체(리스트)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수.
print(min(num_list), max(num_list), end='')
