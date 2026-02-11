import tkinter as tk
from tkinter import filedialog, messagebox
import os
from text_frame import Mid

class FileOperations:
    def __init__(self,master,mid):
        self.editor = mid
        self.current_file = None
        self.master = master
        self.f_name = "Untitled"

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Open", filetypes=[("Text Files","*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.editor.delete_text()
            self.editor.insert_text(content)
            self.current_file = file_path
            # messagebox.showinfo("Opened", f"File opened: {os.path.basename(file_path)}")
            return file_path
        return None

    def save_file(self, event= None):
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.editor.get_text())
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(title="Save", defaultextension=".txt",
                                                 filetypes=[("Text Files","*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.editor.get_text())
            self.current_file = file_path
            # messagebox.showinfo("Saved", f"File saved: {os.path.basename(file_path)}")

    def menu_option(self,open_file_cb,save_cb,save_as_file_cb):
            
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label=" Open          Ctrl+O ",command=open_file_cb)
        file_menu.add_command(label=" Save            Ctrl+S ", command=save_cb)
        file_menu.add_command(label=" Save As ...   Ctrl+Shift+S ", command=save_as_file_cb)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)


# Optional standalone testing
if __name__ == "__main__":

    root = tk.Tk()
    root.title("Test File Operations")
    root.geometry("600x400")
    editor = Mid(root)
    editor.text_bar()
    editor.scroll_bar()
    file_ops = FileOperations(root,editor)
    file_ops.menu_option(file_ops.open_file,file_ops.save_file,file_ops.save_as_file)
    
    root.mainloop()
