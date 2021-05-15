while True :
    try:
        a, b = map(int,input().split())
        print(a + b)
    except:
        break;

# 지정된 케이스 개수가 없으므로 오류 발생 대비를 위한
# 예외 처리가 필요하다. 
