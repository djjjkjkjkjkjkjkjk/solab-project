from tkinter import *
from tkinter import filedialog
from PIL import ImageGrab

def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)

def change_color(new_color):
    global current_color
    current_color = new_color

def change_brush_size(new_size):
    global brush_size
    brush_size = new_size

def clear_canvas():
    canvas.delete("all")

def save_canvas():
    filepath = filedialog.asksaveasfilename(defaultextension=".png")
    if filepath:
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(filepath)

root = Tk()
root.title("그림판")

canvas_width = 800
canvas_height = 600

canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

current_color = "black"
brush_size = 5

color_btn1 = Button(root, text="검정색", command=lambda: change_color("black"))
color_btn1.pack(side=LEFT)

color_btn2 = Button(root, text="빨간색", command=lambda: change_color("red"))
color_btn2.pack(side=LEFT)

clear_btn = Button(root, text="초기화", command=clear_canvas)
clear_btn.pack(side=LEFT)

size_btn1 = Button(root, text="2", command=lambda: change_brush_size(2))
size_btn1.pack(side=LEFT)

size_btn2 = Button(root, text="6", command=lambda: change_brush_size(6))
size_btn2.pack(side=LEFT)

size_btn3 = Button(root, text="8", command=lambda: change_brush_size(8))
size_btn3.pack(side=LEFT)

size_btn4 = Button(root, text="10", command=lambda: change_brush_size(10))
size_btn4.pack(side=LEFT)

save_btn = Button(root, text="저장", command=save_canvas)
save_btn.pack(side=LEFT)

canvas.bind("<B1-Motion>", paint)

root.mainloop()

