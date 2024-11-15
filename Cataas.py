from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        # Делаем запрос и получаем ответ в response
        response = requests.get(url)
        # Для обработки исключения
        response.raise_for_status()
        # В эту переменную (image_data )положим обработанное изображение
        image_data = BytesIO(response.content)
        # В img
        img = Image.open(image_data)
        # Возвращаем img в глобальнюу img
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка {e}")
        # Функция ничего не вернет и выдаст ошибку
        return None


def next_cat():
    img = load_image(url)
    # проверяем, что там есть картинка
    if img:
        # Присваиваем эту картинку на метку
        label.config(image=img)
        # обязательный параметр, чтобы сборщик мусора не убрал её с метки
        label.image = img


window = Tk()
#Заголовок окна
window.title("Cats!")
#Задаем размер окна
window.geometry("600x480")
#Задаем метку на которой выводится изображение
label = Label()
label.pack()
update_button = Button(text = "Следующий котик", command = next_cat)
update_button.pack()
#Адрес по которому будем искать картинки
url = "https://cataas.com/cat"


next_cat()
window.mainloop()
