a, b = input().split()

a = int(a[::-1]) # [::-1] : 역순 설정 
b = int(b[::-1])

if a > b:
    print(a)
else :
    print(b)
