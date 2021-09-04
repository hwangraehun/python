#문제3
#9.4 Write a program to read through the mbox-short.txt
#and figure out who has the sent the greatest number 
# of mail messages.
#The program looks for 'From ' lines
#and takes the second word of those lines as the person
# who sent the mail.
#The program creates a Python dictionary that maps the
#sender's mail address to a count of the number of times 
# they appear in the file.
#After the dictionary is produced, the program reads through
# the dictionary
#using a maximum loop to find the most prolific committer.

name = input("file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
x = 0
counts = dict()
for line in handle :
    if line.find ('From ') : continue
    x = x + 1
    line = line.split()
    mails = line[1]
    counts[mails] = counts.get(mails, 0) + 1
    print("mails", mails)
#print("counts", counts) prints dictionary with email counts and contacts
mostmails = None
prolificomitter = None
for sender,amount in counts.items():
    if mostmails is None or amount > mostmails:
        print("sender, amount", sender, amount)
        mostmails = amount
        prolificomitter = sender
print(prolificomitter, mostmails)


start=int(input('시작단 입력'))
end=int(input('종료단 입력'))
for num in range(start,end+1):
    i=1
    while i<=9:
        print('%dx%d=%d'%(num,i,num*i))
        i+=1
print('종료')
        
        
        alpha={'A':'1!','B':'2@','C':'3#','D':'4$','E':'5%'}
while True:
	code=''
	word=input('대문자 알파벳A~E 단어 입력(종료0)')
	if word =='0':
		break
	for ch in word:
		code+=alpha[ch]
	print('단어:',word,',암호코드:',code,'/n')
print('끝')


start=int(input('시작단 입력'))
end=int(input('종료단 입력'))
for num in range(start,end+1):
    i=1
    while i<=9:
        print('%dx%d=%d'%(num,i,num*i))
        i+=1
print('종료')
        




#문제4
#8.4 Open the file romeo.txt and read 
# it line by line.
#For each line, split the line into a
# list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see 
# if the word is already in the list and 
# if not append it to the list.
#When the program completes, sort and print 
# the resulting words in alphabetical order.
#You can download the sample data at
# http://www.py4e.com/code3/romeo.txt

fname = input("file name")
fh = open(fname)
x = 0
y = 0
oneword = list()
emptylist = list()
newlist = list()
for line in fh:
    x = x + 1
    line = line.rstrip()
    splitline = line.split()
    for element in splitline:
        if element in emptylist : continue
        emptylist.append(element)
        emptylist = sorted(emptylist)
print(emptylist)



#code up 문제5
# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
# 나올 수 있는 모든 경우를 출력해보자.

# 예시
# ...
# for i in range(1, n+1) :
#   for j in range(1, m+1) :
#     print(i, j)
# ...

# 참고
# 위 코드는
# 바깥쪽의 i 값이 1부터 n까지 순서대로 바뀌는 각각의 동안에
# 안쪽의 j 값이 다시 1부터 m까지 변하며 출력되는 코드이다.

# 조건선택 실행구조 안에 다른 조건선택 실행구조를 넣어 처리할 수 있는 것과 마찬가지로
# 반복 실행구조 안에 다른 반복 실행구조를 넣어 처리할 수 있다.

# 원하는 형태로 실행 구조를 결합하거나 중첩시킬 수 있다.

a,b=map(int,input(),split())
for i in range(1,n+1):
    for i in range(1+m):
        print(a,b)

