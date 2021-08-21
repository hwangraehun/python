# ''' hakbun=input('학번입력:')
# name=input('이름 입력:')
# print('학번은',hakbun,'이고,이름은',name,'입니다') '''

# radius=int(input('반지름 길이'))
# area=3.14*radius*radius
# print('원의 길이는 %.2f 입니다'%area)

# width=int(input('가로길이'))
# heigh=int(input('세로 길이'))
# area=width*heigh
# print('가로{},세로{},넓이,{}'.format(width,heigh,area))

# account=100000
# name=input('회원이름')
# account+=1000
# print('%s 회원님에게 1000 지급'%name)
# print('{}장고:{}'.format(name,account))

# tall=int(input('키'))
# ordinary=tall-100*0.9
# print('키%s의 평균체중은%s입니다.'%(tall,ordinary))

# a,b=map(int,input().split())
# print('%s+%s=%s'%(a,b,a+b))
# print('%s/%s=%.1f'%(a,b,a/b))
result=None
# while result !='y':
#     print('파이썬 최고!')
# 	result=input('계속입력하려면 입력:(종료:y)')
# print('종료')
# num=int(input('단 입력:'))
# for i in range(1,10):
#     print('%dx%d=%d'%(num,i,num*i))
# i=1
# num=int(input('단을입력하세요:'))
# while i<=9:
#      print('%dx%d=%d'%(num,i,num*i))
#      i+=1
# print('end')
# while True:
#     num=int(input('번호 입력(종료0):'))
#     if num==0:break
#     print('while  무한루프로 반복중')

# alpha={'A':'1!','B':'2@','C':'3#','D':'4$','E':'5%'}
# while True:
#     code=''
#     word=input('대문자 A~E단어 입력(종료0)')
#     if Word=='0':
#         break
#     for ch in word:
#         code+=alpha[ch]
#     print('단어:',word,',암호코드',code,'/n')
# print('암호코드 변환 프로그램 종료')
#내포가 있는 코드
# num_a=int(input('수를 하나 입력하시오'))
# num_b=int(input('수를 하나 입력하시오'))
# if num_a<0:
#     print('num_a 는 음수입니다')
#     if num_b<0:
#         print('num_b는 음수입니다')
# print('끝')

# num=int(input('수를 하나 입력하시오'))
# if num>0:
#     print('양수를 입력했습니다')
# elif num<0:
#     print('음수를 입력했습니다')
# else:
#     print('영을 입력했습니다')


num_a=5
num_b=7
luck_num=7
# if type(num_a) !=int or type(num_b) != int:
#     print('정수가 아닌값입니다')
# else:
#     if num_a>0 and num_b>0:
#         print('두 정수 모두 양수입니다')
#     elif num_a<0 and num_b <0:
#         print('두 정수 모드 음수입니다')
#     else:
#         print('두 부호가 반대입니다 ')
# if num_a==luck_num or num_b==luck_num:
#     print('게다가 행운의 수를 맞추셨습니다')
# else:
#     print('마음에 봐둔 수가있는데요')
# for v in range(3):
#     print('var v is ',v)

# for ch in "Python is fun so far! 재미있는 파이썬":
#     print('문자:',ch)
# my_string="Python is fun so far! 재미있는 파이썬"
# len_s=len(my_string)
# for i in range(len_s):
#     print("문자:",my_string[i])\

# secret='code'
# guess=input('답을 입력해보세요')
# tries=1
# while guess != secret:
#     print('지금까지',tries,'번 추측에 실패했습니다')
#     guess=input('다른단어를 추측해 보세요')
#     tries+=1
# print('정답')
# for x in range(3):
#     print('var x is',x)

# x=0
# while x<3:
#     print('var x is',x )
#     x+=1


secret='code'
max_tries=100
guess=input('답을 입력해보세요')
tries=1
while guess !=secret:
    print('지금까지',tries,'번 추측에 실패했습니다')
    if tries==max_tries:
        print('추측할 기회를 다 썻습니다')
        break
    guess=input('다른단어를 추측해보세요')
    tries+=1
if tries<= max_tries and guess==secret:
    print('맞추셨습니다')