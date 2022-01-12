from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from PIL import Image, ImageTk, ImageDraw, ImageFont

FONT = ('Arial', 15)
WATERMARK_FONT = ImageFont.truetype('arial.ttf', 50)
WATERMARK_TEXT = 'Aaqil_Modak'


def open_file():
    global WATERMARK_TEXT_COLOR
    type_of_file = [('Jpg Files', '*jpg')]
    file_name = askopenfilename(filetypes=type_of_file, multiple=True)
    col = 1
    row = 3
    for i in file_name:
        img = Image.open(i)
        draw = ImageDraw.Draw(img)
        color = input('Do you want the watermark text to be black or white? B/W: ').upper()
        if color == 'B':
            WATERMARK_TEXT_COLOR = (0, 0, 0)
        elif color == 'W':
            WATERMARK_TEXT_COLOR = (255, 255, 255)
        else:
            print('Invalid Input!')

        draw.text((0, 0), WATERMARK_TEXT, WATERMARK_TEXT_COLOR, font=WATERMARK_FONT)
        file_path2 = askdirectory()
        print(file_path2)
        img.save('{}/watermark.jpg'.format(file_path2))
        img = img.resize((100, 100))
        img = ImageTk.PhotoImage(img)

        label_2 = Label(window)
        label_2.grid(row=row, column=col)
        label_2.image = img
        label_2['image'] = img
        if col == 3:
            row = row + 1
            col = 1
        else:
            col = col + 1


window = Tk()
window.title('Watermark GUI')
window.minsize(width=500, height=400)
window.config(padx=5, pady=50)

# creating labels
label_1 = Label(text='Upload File', font=FONT)
label_1.grid(column=0, row=0)

button_1 = Button(window, text='Choose File', command=open_file)
button_1.grid(column=1, row=1)


window.mainloop()



