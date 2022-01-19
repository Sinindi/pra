def toshi():
    print("당신이 태어난 년도를 입력하세요")
    years = int(input())
    age = 2022 - years +1
    if(age>=20 and age<=26):
        print("대학생")
    elif(age<20 and age>=17):
        print("고등학생")
    elif(age<17 and age>=14):
        print("중학생")
    elif(age<14 and age>=8):
        print("초등학생")
    else:
        print("학생이 아닙니다.")
    
def bai():
    print("구구단 몇단을 계산할까요?")
    a = int(input())
    for i in range(1,11):
        b = a * i 
        print(f"{a} X {i} = {b}")
bai()
