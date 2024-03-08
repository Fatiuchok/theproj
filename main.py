# class Student:
#     def __init__(self):
#         self.height = 170
#
#     height = 160
#     def printer(self):
#         print(self.height)
#
# nick = Student()
# nick.printer()
import random
class Student:
    def __init__(self, name):
        self.name = name
        self.grandness = 50
        self.progress = 0
        self.alive = True
nick = Student("Alex")