# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Horse:  #Класс описывающий лошадь

    def __init__(self):
        self.x_distance = 0  #путь
        self.sound = 'Frrr'   #звук лошади
        super().__init__()
    def run(self, dx):
        self.x_distance += dx   #увеличивает путь на dx

class Eagle:    #Класс орла

    def __init__(self):
        self.y_distance = 0  #высота
        self.sound = 'I train, eat, sleep and repeat'  #звук орла
    def fly(self, dy):   #увеличивает высоту на dy
        self.y_distance += dy

class Pegasus(Horse, Eagle):    #Класс Пегаса
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):  #изменение дистанции
        super().run(dx)
        super().fly(dy)

    def get_pos(self):    #возвращает текущее положение пегаса в виде кортежа
        return self.x_distance, self.y_distance

    def voice(self):  #звук пегаса
        print(self.sound)



p1 = Pegasus()

print(p1.get_pos())
p1.move(20, 30)
print(p1.get_pos())
p1.move(10, 20)
print(p1.get_pos())

p1.voice()
