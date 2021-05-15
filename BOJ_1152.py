string = input("")

if string == " ": #문장 자체가 공백인 경우 
    print(0)
else:
    words = string.split()
    #split은 괄호 안의 내용을 경계로 단어를 구분한다.

    while '' in words: #문장 양쪽에 있는 공백이 없어질 때까지 반복
        words.remove('')

print(len(words)) #len은 길이를 측정하는 함수 
