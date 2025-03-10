#面向对象编程
class Student:
    #添加属性
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')



#调用方式1
stu1 = Student('lyz',19)
Student.study(stu1,'c语言设计')
stu1.play()
#调用方式2
stu2 = Student('qb',18)
stu2.study('c语言设计')