num_list = []
for i in range(9):
    num_list.append(int(input()))

print(max(num_list))
#리스트 내에서의 최대값을 구한다.
print(num_list.index(max(num_list))+1)
#index는 특정 원소의 인덱스값을 구하는 함수.
#+1은 인덱스 번호가 0번부터 시작하므로 1개를 더해줌.
