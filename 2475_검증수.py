result = 0

for n in list(map(int, input().split())):
    result += n**2
print(result%10)

#map : 리스트의 요소를 지정된 함수로 처리해준다.
#map 사용을 위해 리스트를 앞에서 선언.
#여러개의 데이터를 한번에 다른 형태로 변환한다.
# n**2는 n의 제곱.
