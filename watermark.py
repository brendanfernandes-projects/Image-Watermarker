from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

tk = Tk()
tk.title('Image Watermarking App')
tk.config(padx=25, pady=25)

img_file = ''


def file():
    global img_file
    img_file = askopenfilename()


def watermark(final_image, watermark_text, xy_pos):
    global img_file
    image = Image.open(img_file)
    water_mark = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial', 30)
    water_mark.text(xy_pos, watermark_text, font=font, fill='white')
    image.show()
    image.save(final_image)


def img():
    if img_file == '':
        messagebox.showerror('Error','No image was found.')
    else:
        final_image = f'watermarked.jpg'
        watermark_text = text_entry.get()
        watermark(final_image, watermark_text, xy_pos=(50, 50))
        messagebox.showinfo('Completed','Image successfully watermarked!')


title_label = Label(text="Watermark", font=('Roman', 50, "bold"), fg='snow', bg='blue4')
title_label.grid(column=0, row=0, rowspan=4, columnspan=4)
b1 = Button(tk, text="Select", font=20, width=15,
            command=file)
b2 = Button(tk, text="Watermark", font=20, width=15,
            command=img)
b1.grid(column=0, row=5, columnspan=1, padx=25, pady=25)
b2.grid(column=3, row=5, columnspan=1, padx=25, pady=25)

text_label = Label(text="Watermark Text", font=20)
text_label.grid(column=1, row=4, padx=25, pady=25)
text_entry = Entry(width=26)
text_entry.grid(column=1, row=5)
tk.mainloop()
