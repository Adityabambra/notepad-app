import tkinter as tk
from text_frame import Mid

class Bottom:        
    def __init__ (self,master,mid):
        self.text = mid.text
        self.master = master
        self.status_bar = tk.Frame(self.master, bg = "#f0f0f0", height = 24)
        self.status_bar.grid(row = 2, column = 0, sticky = "ew")
        self.status_bar.grid_propagate(False)
        self.size = 12
        self.zoomp = 100

    # create word/character counter label
    def ch_counter (self):
        self.counter = tk.Label(self.status_bar, text= "Words: 0 Characters: 0", anchor= "w", bg="#f0f0f0")
        self.counter.pack(side='left', padx=8)

    # create zoom perecent label
    def zoom_label (self):
        self.zoom_perc = tk.Label(self.status_bar, text="100%", anchor="e", bg="#f0f0f0")
        self.zoom_perc.pack(side='right', padx=8)        

    #ipdate word/ch count
    def update_status(self,event=None):
        text_content = self.text.get("1.0", "end-1c")
        words = len(text_content.split())
        chars = len(text_content)
        self.counter.config(text=f"Words: {words} Characters: {chars}")

    # update zoom percent
    def zoom (self,input):
        if input.keysym in ('equal', 'plus') or input.delta > 0:
            self.size += 2
            self.zoomp += 10
        elif input.keysym == 'minus':
            self.size -= 2
            self.zoomp -= 10
        else:
            return
        self.size = max(6, self.size)
        self.zoomp = max(50,self.zoomp)

        self.text.config(font = ("Arial", self.size))
        self.zoom_perc.config(text = f"{self.zoomp}%")

        return "break"

    # text.bind("<KeyRelease>", update_status)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("status bar test")
    root.geometry("600x500")
    mid=Mid(root)
    mid.text_bar()
    mid.scroll_bar()
    status=Bottom(root,mid)
    status.ch_counter()
    status.zoom_label()
    status.update_status()
    mid.text.bind("<KeyRelease>", status.update_status) 
    root.bind("<Control-MouseWheel>", status.zoom)
    root.bind("<Control-equal>", status.zoom)
    root.bind("<Control-plus>",status.zoom)
    root.bind("<Control-minus>", status.zoom)
    root.mainloop()
