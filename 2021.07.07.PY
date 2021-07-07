# # 미니 자판기 프로그램(오류)
# menu=['콜라','사이다','환타','커피','생수']
# price=[500,500,600,600,400]

# print('**자판기 판매 메뉴**')
# for i in range(5):
#     print('{}:{} {}'.format(i+1,menu[i],price[i]))

# print()                                                                <-왜 쓸모없은 print 넣은걸까

# money=int(input('돈을 투입하세요:'))
# print()                                       

# while True:
#     num=int(input('메뉴선택(종료0)'))
#     if num==0:
#         break
#     if money<price[num-1]:
#         print('잔액부족')
#     else:
#         print(menu[num-1],'구입완료')
#         money=money-price[num-1]                                         <- num-1은 무엇인가
        
#         print('잔액:',money)
#         print()
        
# print('자판기 종료 ,잔액{}반환'. format(money))

#전자 출석부 만들기
# day=int(input('한 학기 수업 주차 입력:'))
# att_book=[0]*day

# for i in range(day):
#     print('%d주차 강의에 출석 하셨나요?'%(i+1))
#     att_book[i]=int(input('출석은 1, 결석은 0>>>'))
    
# print(att_book)

# cnt=att_book.count(0)
# att=att_book.count(1)

# print('결석 횟수 :%d' % cnt)
# print('출석 횟수 :%d' % att)

# 가위 바위 보 게임

# import random

# a=['가위','바위','보']
# human=input('가위,바위,보 중에 하나를 입력하시오:')
# com=a[random.randint(0,2)]  #or random.choice(a)
# print('컴퓨터:%s'%com)
# if human=='가위':
#     if com=='바위':
#         print('컴퓨터 승')
#     elif com=='보':
#         print('당신 승')
#     else:
#         print('비겼습니다')
# elif human=='바위':
#     if com=='가위':
#         print('당신 승')
#     elif com=='보':
#         print('컴퓨터 승')
#     else:
#         print('비겼습니다')
# elif human=='보':
#     if com=='바위':
#         print('당신이 이겼습니다')
#     elif com=='가위':
#         print('컴퓨터 승')
#     else:
#         print('비겼습니다')
# else:
#     print('입력오류')


#연락처 어플 만들기

# print('메뉴를 추가하세요')
# print('1:추가')
# print('0:종료')
# datalist=list()
# while True:
#     menu=int(input('메뉴선택:'))
#     if menu==1:
#         name=input('이름')
#         tel=input('연락처')
#         email=input('email:')
#         datalist.append((name,tel,email))
#         print(datalist)
        
#     elif menu==0:
#         break
#     else:
#         print('입력오류')

#스마트 카페 메뉴 조회 시스템 (어려움)

# menu=[['에스프레소',2000,'커피'],['아메리카노',2500,'커피'],['카푸치노',3000,'커피'],
#       ['카페라떼',3000,'커피'],['모카리떼',3500,'커피'],['바닐라 라떼',3500,'커피'],['소이라떼',3500,'커피'],['피넛라떼',3500,'커피'],['토피넛 라떼',3700,'커피']
#       ['화이트 모카',3700,'커피'],['카라멜마끼아또',4000,'커피'],['프라프치노',4000,'커피'],['핫초코',3500,'음료'],['자몽에이드',3500,'음료'],['레몬에이드',3500,'음료'],
#       ['청포도 에이드',3500,'음료'],['스무디',3500,'음료'],['망고스무디',3500,'음료'],['딸기스무디',3500,'음료'],['초코쿠키',2000,'디저트'],['화이트 쿠키',2000,'디저트'],['피넛쿠키',2000,'디저트']
#       ,['초코케이크',5000,'디저트'],['치즈케이크',5000,'디저트']]
# result=[]
# print('[스마트 카페 메뉴 목록]')
# for i in menu:
#     print(i[0],end='')
#     print('\n')
    
#     while True:
#         choice=eval(input('1.가격별 메뉴 조회 2.종류벌 메뉴 조회 3.주문 0.종료:'))
#         result=[]
#         if choice<0 or choice>3:
#             print('없는 번호')
#             continue
#         elif choice==1:
#             min,max=eval(input('최저가격,최고가격 입력 (예:1000,2000)'))
#             for i in menu:
#                 if i[1]>=min and i[1]<=max:
#                     result.append(i[:2])
#         elif choice==2:
#             category=input('종류별 메뉴 입력')
#             for i in menu:
#                 if i[2]==category:
#                     result.append(i[:2])
#         elif choice==3:
#             order=input('원하는 메뉴 입력')
#             for i in menu:
#                 if i[0]==order:
#                     result.append(i)
#         elif choice==0:
#             print('스마트 카페 메뉴 종료')

#초간단 평점 평균 계산 시스템(오류)
# def subject():
#     while True:
#         title=input=('과목명(0:종료:)')
#         if title=='0':
#             break
#         credit=int(input('학점 수:'))
#         grade=input('취득학점(A,B,C,F):')
#         course.append([title,credit,grade])
        
# def avg_grade():
#     total=0
#     result=0
#     for i in course:
#         if i[2]=='A':
#             total+=i[1]
#             result+=i[1]*4.5
#         elif i[2]=='B':
#             total+=i[1]
#             result+=i[1]*3.5
#         elif i[2]=='C':
#             total+=i[1]
#             result+=i[1]*2.5
#         elif i[2]=='F':
#             total+=i[1]
#     return result/total

# course=[]
# while True:
#     choice=eval(input('1.수강 정보 입력 2. 평균학점 확인 0.종료:'))
#     if choice<0 or choice>3:
#         print('없는 번호')
#         continue
#     elif choice==1:
#         print('<\n수강정보 입력>')
#         subject()
#         print('<수강정보 입력 종료\n>')
#     elif choice==2:
#         print('\n<수강 강좌 목록>')
#         print('과목명\t학점수\t학점')
#         print('-'*20)
#         gpa=avg_grade()
#         for i in course:
#             print(i[0], '\t', i[1],'\t',i[2])
#         print('\n 평균학점:%2.f\n'% gpa)
#     elif choice==0:
#         print('종료')
#         break

# if 3 in range(5):
#     print('There is 3')

# for i in range(10):
#     print(i,)

# for i in range(100):
#     if i % 7 == 0:
#         print(i)

# for item in range(2,20):
#     for each in range(1,10):
#         print('%sx%s=%s'%(item,each,each*item))

#부가세 구하기 
# y = lambda x : 3* x
# print(y(333))

# add=lambda a,b: a+b
# print(add(10,3))

# while True: = while 1 :

# import _random
# for event in pygame.event.get():
#     if event.type ==pygame.QUIT:
#         sys.exit()

# screen.fill((255,255,255))

#도서관 정보 검색 시스템
# from csv import*
# file=open('libary.csv', 'r')
# read_file=reader(file)
# libary_list=[]
# for line in rea_line

# score=[70,90,60,100,50]
# cnt=0
# for i in range(5):
#     if score[i]>=70:
#         cnt+=1
    
# print('count:',cnt)

# s=int(input('start num:'))
# e=int(input('end num:'))

# total=0
# odd=0
# even=0
# for i in range(s,e+1):
#     total+=i
#     if i%2==0:   
#         even+=i
#     else:
#         odd+=i
        
        
# print('전체 합계:',total)
# print('짝수의 합:',even)
# print('홀수의 합:',odd)

# score=[85,95,70,50,100]
# n=0
# print('코딩시험 결과')
# print('-'*30)
# for s in score:
#     n+=1
#     if s>=90:
#         result='LEVEL1'
#     elif s>=80:
#         result='LEVEL2'
#     elif s>=70:
#         result='LEVEL3'
#     else:
#         result='FAIL'

# print('{}번 학생의 점수는 {}입니다'.format(n,s))
# print('결과는 {}입니다.'.format(result))
# print()

# score=[85,95,70,50,100]
# n=0
# print('코딩시험 결과')
# print('-'*30)
# for s in score:
#     n+=1
#     if s>=90:
#         result='LEVEL1'
#         print('{}번 학생의 점수는 {}입니다\n.결과는{}입니다.'.format(n,s,result))
#     elif s>=80:
#         result='LEVEL2'
#         print('{}번 학생의 점수는 {}입니다\n.결과는{}입니다.'.format(n,s,result))
#     elif s>=70:
#         result='LEVEL3'
#         print('{}번 학생의 점수는 {}입니다\n.결과는{}입니다.'.format(n,s,result))
#     else:
#         result='FAIL'
#         print('{}번 학생의 점수는 {}입니다\n.결과는{}입니다.'.format(n,s,result))

# print('{}번 학생의 점수는 {}입니다\n.결과는{}입니다.'.format(n,s,result))
# print('결과는 {}입니다.'.format(result))
# print()
# import random
# print('주사위 게임 시작')
# throw=input('Enter을 치세요')
# while throw !=0:
#     com=random.randint(1,6)
#     user=int(input('num:'))
#     if com>user:
#         win='com'
#     else:
#         win='user'
#     print('com{}:user{}, {}win'.format(com,user,win))
#     throw=input('재시작:Enter, 종료:0')
