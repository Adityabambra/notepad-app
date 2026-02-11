import tkinter as tk
from text_frame import Mid

class Top:
    def __init__ (self,master):
        self.master = master
        # self.text = mid.text
        self.sub_frame = tk.Frame(self.master, bg = "#f0f0f0")
        self.sub_frame.grid(row = 0, column = 0, sticky = 'ew')

    # subject label

    def sub_label (self):
        self.label = tk.Label(
            self.sub_frame,
            text = "Subject",
            bg = "#f0f0f0",
            font = ("Arial", 14)
        )
        self.label.pack(side = 'left')
    
    # Subject Heading/ Real subject

    def sub_heading_entry (self):
        self.sub_head = tk.Entry(self.sub_frame, font = ("Arial", 12))
        self.sub_head.pack(side = 'left', fill = 'x', expand = True)

    # Move cursor to text frame
    
    # def move_to_text (self,event):
    #     self.text.focus_set()
    #     return "break"
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("subject bar test")
    root.geometry("600x500")
    mid=Mid(root)
    mid.text_bar()
    mid.scroll_bar()
    status = Top(root,mid)
    status.sub_label()
    status.sub_heading_entry()
    # status.sub_head.bind("<Return>",status.move_to_text)
    root.mainloop()
