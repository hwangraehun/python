# 클래스
# class Name:
#     pass

# 인스턴스
# a=Name()

# 클래스 생성자1
# class Name:
#     def __init__(self):
#         print('하이')
# a=Name()

# 클래스 생성자2
# a=Name('이름','나이','성별')

# class Name:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
        
# a=Name('래훈',22,'남자')
# print(a.name,a.age,a.sex)

# 인스턴스 속성 접근
# a.name....

# 클래스 메소드
# 이름나이 성별 한번에 입력하는 who() 메소드 만들기
class Name:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {0} 나이: {1} 성별: {2}" .format(self.name, self.age, self.sex))
        
a = Name("래훈", 22, "남자")
a.who()
print(a.who())

# a= Human("모름", 0, "모름")
# a.setInfo("아름", 25, "여자")