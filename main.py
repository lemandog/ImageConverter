import tkinter
from tkinter import *
from tkinter import ttk

import PIL.Image
from PIL import ImageTk
from tkinterdnd2 import *
from PIL import *

ws = TkinterDnD.Tk()
ws.resizable(height=False, width=False)
ws.title("Конвертер Изображений")
ws.geometry("400x400")
ws.config(bg="#fcb103")

formats = (
    "jpeg",
    "tif",
    "tiff",
    "bmp",
    "gif",
    "png",
    "eps",
    "raw",
    "cr2",
    "nef",
    "orf",
    "sr2",
    "webp",
    "ico"
)

frame = Frame(ws)
frame.pack()
label = Label(frame, text="ПЕРЕТАЩИ ИЗОБРАЖЕНИЯ СЮДА")
label.pack(side=TOP)

canvas = Label(frame, height=400, width=400, background="DARKGRAY")

widget_var = formats
combobox = ttk.Combobox(frame, width=27, values=formats)
combobox.set(formats[0])
combobox.pack(side=TOP)


def convertImg(event):
    with open(event.data, "r") as file:
        try:
            img = PIL.Image.open(file.name).convert("RGB")

            ph = img.resize((400, 400), Image.ANTIALIAS)
            ph = ImageTk.PhotoImage(ph)

            canvas.configure(image=ph)
            canvas.image = ph

            label.config(text=file.name)

            saveString = file.name
            saveString = saveString.replace(".", "")
            img.save(saveString + "." + combobox.get(), format=combobox.get())
        except UnidentifiedImageError:
            label.config(text="Неизвестный формат изображения, или оно повреждено")


canvas.pack(side=RIGHT)
canvas.drop_target_register(DND_FILES)
canvas.dnd_bind("<<Drop>>", convertImg)

ws.mainloop()
