# stock 클래스  (stock 주식회사 자본 뜻함)

# 1. 클래스 생성
# class Name:
#     pass    

# 2.생성자 정의

# 객체가 생성될때 정보 입력받는것

# class Name:
#     def __init__(self, color, code):
#         self.color=color
#         self.code=code
        
# 사과=Name('red','1')
# print(사과.color)
# print(사과.code)

# 메서드 
# 객체의 산술계산
# (종족명 입력 받는것)

class Name:
    def __init__(self, color, code):
        self.color = color
        self.code = code

    def set_name(self, name):
        self.name = name

a = Name(None, None)
a.set_name("포도") 
print(a.name)

