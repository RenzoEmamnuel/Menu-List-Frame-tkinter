from tkinter import *
from tkinter import filedialog, simpledialog, messagebox

root = Tk()
root.geometry("500x500")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            data = file.read()
            list_box.delete(0, END)
            for line in data.split('\n'):
                list_box.insert(END, line)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            data = '\n'.join(list_box.get(0, END))
            file.write(data)

def add_item():
    item = simpledialog.askstring(" ", "Enter item:",)
    if item:
        list_box.insert(END, item)

def delete_item():
    selected_indices = list_box.curselection()
    if selected_indices:
        for index in selected_indices[::-1]:
            list_box.delete(index)

def edit_item():
    selected_indices = list_box.curselection()
    if selected_indices:
        item = simpledialog.askstring("Edit Item", "Enter new item value:", initialvalue=list_box.get(selected_indices[0]))
        if item:
            list_box.delete(selected_indices[0])
            list_box.insert(selected_indices[0], item)

def show_help():
    messagebox.showinfo("Help", "This is a simple list management application.\n\n"
                                 "File menu:\n"
                                 " - Open: Load data from a file\n"
                                 " - Save: Save current list data to a file\n\n"
                                 "Edit menu:\n"
                                 " - Add: Add new items to the list\n"
                                 " - Delete: Remove selected items from the list\n"
                                 " - Edit: Modify existing items in the list\n\n"
                                 "Help menu:\n"
                                 " - Help: Display this information")

main_menu = Menu(root)

menu_file = Menu(main_menu, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
main_menu.add_cascade(label="File", menu=menu_file)

menu_edit = Menu(main_menu, tearoff=0)
menu_edit.add_command(label="Add", command=add_item)
menu_edit.add_command(label="Delete", command=delete_item)
menu_edit.add_command(label="Edit", command=edit_item)
main_menu.add_cascade(label="Edit", menu=menu_edit)

menu_help = Menu(main_menu, tearoff=0)
menu_help.add_command(label="Help", command=show_help)
main_menu.add_cascade(label="Help", menu=menu_help)

root.config(menu=main_menu)

frame_1 = Frame(root, width=480, height=490, padx=10, pady=10, bg="#f0b7b3")
frame_1.pack()
frame_1.pack_propagate(False)
list_box = Listbox(frame_1,width=50,height=25)
list_box.pack(pady=25)

root.mainloop()
