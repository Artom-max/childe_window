from tkinter import *


class Child_window:
    def __init__(self, perent, width, heigth, title, resizable=(False, False), icon='1.ico'):
        self.root = Toplevel(perent)  # метод tkinter Toplevel позваляет создавать дочерние окна(зависящие от главного)
        self.root.title(title)
        self.root.geometry(f'{width}x{heigth}+1000+90')
        self.root.resizable(resizable[0], resizable[1])
        self.root.iconbitmap(icon)
        self.grab_focus()
        self.face_image1 = PhotoImage(file=r'12.png')
        self.label2 = Label(self.root, image=self.face_image1, relief=GROOVE)
        self.lable2.image = self.face_image1
        self.label2.pack()

    def grab_focus(self):
        self.root.grab_set()  # забирает фокус на этот объект(окно) похоже на всплывающие окна для ввода паролей
        self.root.focus_set()  # то же саоме только этот метод захватывает фокус и не позволяет использовать другое окно
        self.root.wait_window()  # метод ждет пока будет уничтожено текущий объект не возобновляя работы при этом не
        # влияя на основной цикл

    def draw_image(self):
      pass
