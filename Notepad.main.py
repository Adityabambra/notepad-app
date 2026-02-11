import tkinter as tk
import os
from tkinter import messagebox
from file_options import FileOperations
from subject import Top
from text_frame import Mid
from status import Bottom

def main():
    is_modified = False          # track unsaved changes
    current_file = None         # track current file path

    root = tk.Tk()
    root.title("Untitled-Notepad")
    root.geometry("600x400")
    root.configure(bg="#f0f0f0")

    icon = tk.PhotoImage(file="notepad_icon.png")
    root.iconphoto(True, icon)

    # ---------- GRID LAYOUT ----------
    root.grid_rowconfigure(0, weight=0)   # Subject
    root.grid_rowconfigure(1, weight=1)   # Text
    root.grid_rowconfigure(2, weight=0)   # Status
    root.grid_columnconfigure(0, weight=1)

    # ---------- SUBJECT ----------
    top_sub = Top(root)
    top_sub.sub_label()
    top_sub.sub_heading_entry()

    # ---------- TEXT ----------
    mid = Mid(root)
    mid.text_bar()
    mid.scroll_bar()
    mid.text.config(yscrollcommand=mid.scroll.set)

    top_sub.sub_head.bind("<Return>", mid.move_to_text)

    # ---------- FILE OPERATIONS ----------
    file_ops = FileOperations(root, mid)

    def open_file_wrapper(event=None):      # Change modified and notepad title on opening a file
        nonlocal current_file, is_modified
        path = file_ops.open_file()   
        if path:
            current_file = path
            is_modified = False
            filename = os.path.basename(path).replace(".txt","")
            root.title(f"{filename}-Notepad")

    def save_wrapper(event=None):       # Change modified and notepad title on saving a file
        nonlocal is_modified, current_file
        path = file_ops.save_file(current_file)
        if path:
            current_file = path
            is_modified = False
            filename = os.path.basename(path)
            root.title(f"{filename}-Notepad").replace(".txt","")

    def save_as_wrapper(event=None):      # Change modified and notepad title on saving as a file
        nonlocal is_modified, current_file
        path = file_ops.save_as_file()
        if path:
            current_file = path
            is_modified = False
            filename = os.path.basename(path)
            root.title(f"{filename} - Notepad")
            

    file_ops.menu_option(open_file_wrapper,save_wrapper, save_as_wrapper)
    root.bind("<Control-s>", save_wrapper)
    root.bind("<Control-o>",open_file_wrapper)
    root.bind("<Control-Shift-S>",save_as_wrapper)

    # ---------- STATUS BAR ----------
    last = Bottom(root, mid)
    last.ch_counter()
    last.zoom_label()
    mid.text.bind("<KeyRelease>", last.update_status)

    root.bind("<Control-MouseWheel>", last.zoom)
    root.bind("<Control-equal>", last.zoom)
    root.bind("<Control-plus>", last.zoom)
    root.bind("<Control-minus>", last.zoom)

    # ---------- TRACK MODIFICATIONS ----------
    def mark_modified(event=None):
        nonlocal is_modified
        is_modified = True

    mid.text.bind("<Key>", mark_modified)

    # ---------- EXIT CONFIRM ----------
    def confirm_exit():
        if not is_modified:
            root.quit()
            return

        result = messagebox.askyesnocancel(
            title="Notepad",
            message="Save changes before exit?"
        )

        if result is True:
            save_wrapper()
            root.quit()
        elif result is False:
            root.quit()
        else:
            return

    root.protocol("WM_DELETE_WINDOW", confirm_exit)

    root.mainloop()

if __name__ == "__main__":
    main()
