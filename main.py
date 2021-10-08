from tkinter import *

import PIL.Image
from tkinterdnd2 import *
from PIL import *

ws = TkinterDnD.Tk()
ws.resizable(height = False, width = False)
ws.title('Конвертер Изображений')
ws.geometry('400x400')
ws.config(bg='#fcb103')

formats = (
    '.tif',
    '.tiff',
    '.bmp',
    '.jpg,',
    '.jpeg',
    '.gif',
    '.png',
    '.eps',
    '.raw',
    '.cr2',
    '.nef',
    '.orf',
    '.sr2',
    '.webp')

frame = Frame(ws)
frame.pack()
label = Label(frame, text='ПЕРЕТАЩИ ИЗОБРАЖЕНИЯ СЮДА')
label.pack(side=TOP)
canvas = Label(frame, height=300, width=300)


def convertImg(event):
    if event.data.endswith(formats):
        with open(event.data, 'r') as file:
            try:
                img = PIL.Image.open(file.name).convert('RGB')
                print(file.name)
                saveString = file.name
                saveString = saveString.replace(".", "")
                img.save(saveString + 'Conv.png', format='png')
            except UnidentifiedImageError:
                label.config(text="Неизвестный формат изображения, или оно повреждено")


canvas.pack(side=LEFT)
canvas.drop_target_register(DND_FILES)
canvas.dnd_bind('<<Drop>>', convertImg)

ws.mainloop()
