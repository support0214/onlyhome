#올바른 변수 이름
 # apple = "사과"
 # apples = "사과들"
 # apple3 = "사과3개"

#잘못된 변수 이름
 # 3apple = "3개의 사과"
 # red apple = "빨간 사과"
 # apple!= "사과!"

#int(정수)형 
#a = 5
#b = -15
#c = 0
#print(type(a), type(b), type(c))

#float(실수)형
#d = 5.5
#e = -5.5
#f = 0.0
#print(type(d), type(e), type(f))

#과학적 표기법
#123456.7 = 1.234567 * 10^5
#g = 1.234567e5
#print(g)

#complex 자료형 + 복소수와 복소수 연산들이 필요할 때 사용하는 자료형

#string 문자, 문자열
#text = "String \"Data\" Type"

# and or not

# index
#weather = "맑음"
#temperature = 20
#chance_shower = 33.5

#print("오늘의 날씨는", weather, "기온은", temperature,"도 입니다.")
#print("오늘의 날씨는 %s 기온은 %d도 입니다."%(weather, temperature))
#print("오늘의 날씨는 {} 기온은 {}도 비가 내릴 확률은 {}%입니다.".format(weather,temperature,chance_shower))

#NameError
#age
#addres

# print("안녕하세요 제 이름은 {0}입니다. 나이는 {1}살이며 사는 곳은 {2}입니다.".format(NameError, age, address))
# f-string
#weather = "맑음"
#temperature = 20

#print(f"오늘의 날씨는 {weather}이며, 기온은 {temperature}도입니다.")

#text = "www.GOOGLE.com"
#print(len(text))

#txt_capitalize = text.upper()
#print(text.upper())
#print(text.lower())

#g_find = text.find('G')
#g_cnt = text.count('G')

#number = [0,1,2,3,4,5,6,7]

#print(number[0]) # 시퀀스
#print(number[3:5]) # 슬라이싱

#list_lang = ["JAVA", "C", "Python", "Go"]

#print(len(list_lang))

# text = ["가", "나", "다"]
# print(text[0])
# # print(text[-1])
# print(text[-2]) 

#list [] 고정값 X tuple () 고정값 o
#numbers = (1, 2, 3, 4, 5)
#print(numbers.index(5))

# coffee = {"Java":2500,"Americano":2500,"Latte":3000} 딕셔너리(dictionary)
# coffee["Moca"] = 3000
# print(coffee.values())
# print(coffee.items())

# week={"월", "화", "수","목","금","토"}
# week.add("화") #숫자 문자 True 튜플 추가가능, [1,2,3] {keys:value} 추가X

# week=set(["월","화","수","목","금"])
# print(week)

# a={1,2,3,4,5}b={3,4,5,6,7}a.remove(4)print(a)

#input
# number = float(input("첫번째 실수를 입력해주세요>"))
# number1 = float(input("두번째 실수를 입력해주세요 >"))
# print(number + number1)

# study_time = int(input("오늘의 공부시간을 입력해주세요>"))
# if 6 >= study_time >= 3:
#     print("오늘은 파이썬 공부를 합시다 !")
# else :
#     print("다 뻥이야")

# number = input("주민번호를 입력해주세요 >")

# odd = int(number[7])
# if odd % 2 == 0:
#     print("여성입니다.")
# else :
#     print("남성입니다.")

# lunch = input("점심메뉴를 골라주세요(제육덮밥, 돈까스, 김밥)>")

# if lunch == "제육덮밥":
#     print("제육덮밥 먹는다.")
# elif lunch =="돈까스":
#     print("돈까스 먹는다.")
# elif lunch =="김밥":
#     print("김밥 먹는다.")
# else:
#     print("점심을 굶는다.")

# number = int(input("정수를 입력해주세요 : "))
# if number % 3 == 0 and number % 2 == 0:
#         print("3의 배수이면서 짝수입니다.")
# elif number % 3 !=0 : 
#     print("3의 배수가 아닙니다.")
# else :
#     print("짝수가 아닙니다.")


# num = 1
# while num <= 5:
#     num += 1
#     print(num)

# fruits = ["사과", "키위", "바나나", "사과", "바나나", "망고"]
# print(fruits)
# fruit = input("빼낼 과일을 입력해주세요 > ")

# while fruit in fruits:
#     fruits.remove(fruit)

# print(fruits)
# print("{}를 모두 제거했습니다.".format(fruit))


# if, while 문 사용한 예제문제
# min_num = int(input("최소값을 입력 : "))
# max_num = int(input("최대값을 입력 : "))

# odd_list = []
# even_list = []

# num = min_num

# if min_num < max_num:
#     while num <= max_num:
#         if num % 2 == 0:
#             even_list.append(num)
#         else:
#             odd_list.append(num)
#         num += 1
#     print("{}부터 {}까지의 짝수는 {}입니다.".format(min_num, max_num,even_list))
#     print("{}부터 {}까지의 홀수는 {}입니다.".format(min_num, max_num,odd_list))
    
# else:
#     print("최댓값 {}이 최소값{}보다 크지 않습니다".format(max_num, min_num))

#for문
# for i in range(1, 10+1):
#     print(i)
sum =1

for i in range(1, 30+1):
    if i % 3 == 0:
        sum += i
print(sum)