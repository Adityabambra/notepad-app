import tkinter as tk 

class Mid:
    def __init__ (self,master):
        self.master = master
        self.text_container = tk.Frame(self.master)
        self.text_container.grid(row = 1, column = 0, sticky = 'nsew')
         
        self.text_container.grid_rowconfigure(0, weight = 1)
        self.text_container.grid_columnconfigure(0, weight = 1)
        # self.text=None

    # create text frame

    def text_bar (self):
        self.text=tk.Text(self.text_container, font = ("Consolas", 12) ,undo = True)
        self.text.grid(row =  0, column = 0, sticky = "nsew")

    # create scroll bar

    def scroll_bar(self):
        self.scroll = tk.Scrollbar(self.text_container, command= self.text.yview, width = 15)
        self.scroll.grid(row = 0, column = 1, sticky = 'ns')

    # move cursor from subject to text
    def move_to_text (self,event):
        self.text.focus_set()
        return "break"
    
    
    def get_text(self):
        return self.text.get("1.0", tk.END)

    def insert_text(self, text, index=tk.END):
        self.text.insert(index, text)

    def delete_text(self, start="1.0", end=tk.END):
        self.text.delete(start, end)

    
    
if __name__ == "__main__":
    root=tk.Tk()
    root.title("Text,scroll bar check")
    root.geometry("600x500")
    
    mid = Mid(root)
    mid.text_bar()
    mid.scroll_bar()
    root.mainloop()


