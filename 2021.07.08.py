# menu={'라면':3000,'떡볶이':4000,'김밥':2000,'햄버거':5000}
# for i in menu.items():
#     print('{}-{}'.format(i[0],i[1]))
    
#     while True:
#         s=input('seach menu:')
#         if s=='q':break
#         print(menu.get(s,'not found'))

# n=0
# club=[]

# while True:
#     num=int(input('학번:'))
#     if num==0:break
#     name=input('이름:')
#     dept=input('학과:')
#     phone=input('연락처:')
#     addr={'학번':num,'이름':name,'학과':dept,'연락처':phone}
#     club.append(addr)
#     print('{}학생 정보 저장'.format(n+1))
#     print('{}'.format(club[n]))
#     n+=1

# score=[]
# p=0
# f=0
# cnt=int(input('수강 과목 수:'))

# for i in range(cnt):
#     s=int(input('score %d:'%(i+1)))
#     score.append(s)
    
# for i in range(cnt):
#     if score[i]>=80:
#         p+=1
#     else:
#         f+=1
# print('pass: ',p)
# print('fail: ',f)

# a=2
# b=2
# print(b-a)

# minutes_to_convert=int(input('분을 입력하세요'))

# hours_decimal=minutes_to_convert/60
# hours_part=int(hours_decimal)

# minutes_decimal=hours_decimal-hours_part
# minites_part=round(minutes_decimal*60)

# print(hours_part)
# print('시간')
# print(minites_part)
# print('분')

# minutes_to_convert=123

# hours_decimal=minutes_to_convert/60
# hours_part=int(hours_decimal)

# minutes_part=minutes_to_convert%60

# print(hours_part)
# print('시간')
# print(minutes_part)
# print('분')

#온도를 화씨로

# fahrehiet=75
# temper=fahrehiet*1.8/+32

# print(temper)
# f=75
# c=(f-32)/1.8
# print(round(c))

# mile=5
# km=mile/0.62137
# meter=1000*km

# print(mile)
# print('마일')
# print(km)
# print('킬로미터')
# print(meter)
# print('미터')
# a='python 4 ever&EVER 최고!'
# print('on' in a)
# print(""in a)
# print('2*2' in a)
# print('최고' in a)
# print('pt' in a)

# a='Raing in the sprint time. 미세먼지 안녕!'
# print(a.replace('R','r'))

# a=(1,2,[1,2,3])
# print(a.count(1))

# print(len(('hi','hello','hey')))
# print(len(((1,2),)))
# a=(3,(3,('5',7),9),'a')
# print(a[1:2][1])
# a=0
# t=(True,'True')
# print(t[a])


# print(len('abc')*('no',))
# print(2*('no','no','no'))
# print((0,0,0)+(1,))
# print((1,1)+(1,1))

# long='hello'
# short='hi'
# (short,long)=(long,short)

# print(long)
# print(short)
# b='is the new cool'
# print(b.capitalize()+b)

# user_input=input('제곱을 계산할 수를 입력하세요: ')
# num=int(user_input)
# print(num*num)

# num=float(input('첫번째 수를 입력하세요: '))
# num2=float(input('두번째 수를 입력하세요: '))
# print(num,'x',num2,'=',num*num2)

# b=int(input('수를 입력하세요: '))
# e=int(input('수를 입력하세요: '))
# print(b**e)


# name=input('이름을 입력하세요: ')
# age=int(input('나이를 입력하세요: '))
# print('안녕 {} 당신은 25년 후 나이는 {}살이야!'.format(name,age+25) )

print('Welcom to the Mashup Game!')
name1=input('Enter one full name (FIRST LAST): ')
name2=input('Enter another full name (FIRST LASTE): ')

space=name1.find(' ')
name1_first=name1[0:space]
name1_last=name1[space+1:len(name1)]
space1=name2.find(' ')
name2_first=name2[0:space1]
name2_last=name2[space1+1:len(name2)]
print(name1_first)
print(name1_last)
print(name2_first)
print(name2_last)

len_name1_first=len(name1_first)
len_name1_last=len(name1_last)
len_name2_first=len(name2_first)
len_name2_last=len(name2_last)
index_name1_first=int(len_name1_first/2)
index_name2_first=int(len_name2_first/2)
index_name1_last=int(len_name1_last/2)
index_name2_last=int(len_name2_last/2)
lefthalf_name1_first=name1_first[0:index_name1_first]
righthalf_name1_first=name1_last[index_name1_first:len_name1_first]
lefthalf_name2_first=name2_first[0:index_name2_first]
righthalf_name2_first=name2_last[index_name2_first:len_name2_first]
lefthalf_name1_last=name1_last[0:index_name1_last]
righthalf_name1_last=name1_last[index_name1_last:len_name1_last]
lefthalf_name2_last=name2_last[0:index_name2_last]
righthalf_name2_last=name2_last[index_name2_last:len_name2_last]

new_name1_first=lefthalf_name1_first.capitalize()+righthalf_name1_first.lower()
new_name1_last=lefthalf_name1_last.capitalize() +righthalf_name1_last.lower()

new_name2_first=lefthalf_name2_first.capitalize()+righthalf_name2_first.lower()
new_name2_last=lefthalf_name2_last.capitalize() +righthalf_name2_last.lower()

print('All done! her are two possibilities, pock the one you lke best!')
print(new_name1_first,new_name1_last)
print(new_name2_first,new_name2_last)