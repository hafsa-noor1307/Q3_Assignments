# graphics.py
import tkinter as tk

class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack()
        self.mouse_x = 0
        self.mouse_y = 0
        self.last_click = (0, 0)
        self.canvas.bind("<Motion>", self._on_mouse_move)
        self.canvas.bind("<Button-1>", self._on_click)
        self.root.update()

    def _on_mouse_move(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def _on_click(self, event):
        self.last_click = (event.x, event.y)

    def get_mouse_x(self):
        return self.mouse_x

    def get_mouse_y(self):
        return self.mouse_y

    def get_last_click(self):
        return self.last_click

    def wait_for_click(self):
        self.root.wait_variable(tk.IntVar())

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

    def set_color(self, object_id, color):
        self.canvas.itemconfig(object_id, fill=color, outline=color)

    def moveto(self, object_id, x, y):
        coords = self.canvas.coords(object_id)
        width = coords[2] - coords[0]
        height = coords[3] - coords[1]
        self.canvas.coords(object_id, x, y, x + width, y + height)
        self.root.update()

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)
