from tkinter import *
from child_window import Child_window


class Window:
    def __init__(self, width, heigth, title, resizeble=(False, False), icon='1.ico'):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{heigth}+1000+90')
        self.root.resizable(resizeble[0], resizeble[1])
        self.root.iconbitmap(icon)
        self.label = Label(self.root, text="Я надпись", bg="#e84ae3", relief=SUNKEN, wraplength=55, font="Arial 10")
        # создание лэйбла первый параметр
        # показывает на каком объекте он будет, задется текст, бэкграунд и другое отображаться, а остальные побочные,
        # такие как текст, шрифт и т.д, но его еще нужно прорисовать, relife(рельеф) меняет обводку wraplength=25,
        # показывает сколько пикселей выделено на одну строчку
        self.face_image = PhotoImage(file=r'123.png')  # 'загрузка изображения в переменную',
        self.label1 = Label(self.root, image=self.face_image, relief=GROOVE)  # загрузка в виджет
        self.draw_widjet()

    def draw_widjet(self):
        self.label.pack(anchor=NW, padx=20, pady=10)  # прорисовка виджетов в порядке очереди(возможно наслоение)
        self.label1.pack(anchor=NW, padx=20, pady=100)  # прорисовка виджета, параметры padx и pady отвечают за отступ

    def create_child(self, width, heigth, title, resizable=(False, False)):
        Child_window(self.root, width, heigth, title, resizable)

    def run(self):

        self.root.mainloop()


if __name__ == "__main__":  # эта строчка гарантирует запуск окна из этого файла с заданными параметрами, а в других
    # где класс импортируется будут использованные другие заданные параметры
    window = Window(400, 600, "Главное окно")
    window.create_child(300, 300, "Дочернее окно")
    window.draw_widjet()
    window.run()
# window = Tk()
# window.title("Приложение графического интерфейса")  # задает окну имя
# window.geometry("400x600+1000+90")  # ширина, высота, отсуп с нулевой координаты
# window.resizable(False, False)  # запрещает пользователю изменять размеры окна
# window.iconbitmap("1.ico")  # задает программе иконку
#
#
# window.mainloop()
