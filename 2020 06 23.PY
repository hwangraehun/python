Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> (100>200)or(200>100)
True
>>> (100>200)and(200>100)
False
>>> not(100>200)
True
>>> #여러조건 논리연산자
>>> #숫자비교 비교논산자
>>> #조건 if
>>> has_Owner=True
>>> if has_Owner==True:
	print('통행료를 지불하세요!')

	
통행료를 지불하세요!
>>> has-Owner=False
SyntaxError: cannot assign to operator
>>> has_Owner=False
>>> if has_Owner==True:
	print('통행료를 지불하시오')

	
>>> if has_Owner:
	print(통)

	
>>> has_Owner=True
>>> if has_Owner:
	print('통')

	
통
>>> #if 참일떄 실행
>>> #else 거짓일떄 실행
>>> has_Owner=False
>>> if has_Owner==True:
	print('통행료를 지불하시오')
else:
	print('야호 통과')

	
야호 통과
>>> #Ohas_wner 입력값 받기
>>> 예
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    예
NameError: name '예' is not defined
>>> 아니오
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    아니오
NameError: name '아니오' is not defined
>>> ㅇ
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    ㅇ
NameError: name 'ᄋ' is not defined
>>> #if elif else
>>> has_owner=input('땅 주인이 있나요?(예/아니요)')
땅 주인이 있나요?(예/아니요)
>>> 
KeyboardInterrupt
>>> 예
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    예
NameError: name '예' is not defined
>>> 
====================================================================== RESTART: C:/Users/ghkdh/Desktop/if-elif-else.py =====================================================================
땅 주인이 있나요?(예/아니요)예
통행료를 지불하세요
>>> 아니오
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    아니오
NameError: name '아니오' is not defined
>>> 
====================================================================== RESTART: C:/Users/ghkdh/Desktop/if-elif-else.py =====================================================================
땅 주인이 있나요?(예/아니요)아니오
통과
>>> 
====================================================================== RESTART: C:/Users/ghkdh/Desktop/if-elif-else.py =====================================================================
땅 주인이 있나요?(예/아니요)네
잘못 입력하였습니다
>>> 