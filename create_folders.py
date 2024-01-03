import os
import tkinter as tk
from tkinter import filedialog, Label, Entry, Button, StringVar, Listbox, ttk
from calendar import month_abbr

def create_folders(directory, start_month, end_month, year, detail, date_format, detail_position):
    for month in range(int(start_month), int(end_month) + 1):
        folder_name = format_folder_name(month, year, date_format, detail, detail_position)
        path = os.path.join(directory, folder_name)
        os.makedirs(path, exist_ok=True)

def format_folder_name(month, year, date_format, detail, detail_position):
    month_year_format = {
        'MM_YYYY': f"{str(month).zfill(2)}_{year}",
        'YYYY_MM': f"{year}_{str(month).zfill(2)}",
        'MMM_YYYY': f"{month_abbr[month]}_{year}",
        'YYYY_MMM': f"{year}_{month_abbr[month]}"
    }
    base_name = month_year_format[date_format]
    return f"{detail}_{base_name}" if detail and detail_position == "Beginning" else f"{base_name}_{detail}" if detail else base_name

def update_preview(start_month, end_month, detail, preview_list, year, date_format, detail_position):
    preview_list.delete(0, tk.END)
    for month in range(int(start_month), int(end_month) + 1):
        folder_name = format_folder_name(month, year, date_format, detail, detail_position)
        preview_list.insert(tk.END, folder_name)

def main():
    root = tk.Tk()
    root.title("Folder Creation Tool")

    def on_directory_selected():
        if dir_path.get():
            update_button.config(state='normal')
            confirm_button.config(state='normal')

    def on_confirm():
        create_folders(dir_path.get(), start_month_var.get(), end_month_var.get(), year_var.get(), detail_var.get(), date_format_var.get(), detail_position_var.get())
        print(f"Folders created in {dir_path.get()}")

    def clear_entries():
        dir_path.set('')
        start_month_var.set('')
        end_month_var.set('')
        year_var.set('')
        detail_var.set('')
        date_format_var.set('MM_YYYY')
        detail_position_var.set('End')
        preview_list.delete(0, tk.END)
        update_button.config(state='disabled')
        confirm_button.config(state='disabled')

    dir_path = StringVar()
    start_month_var = StringVar(value='')
    end_month_var = StringVar(value='')
    year_var = StringVar(value='')
    detail_var = StringVar()
    date_format_var = StringVar(value='MM_YYYY')
    detail_position_var = StringVar(value='End')

    Label(root, text="Directory:").pack()
    Entry(root, textvariable=dir_path).pack()
    Button(root, text="Select Directory", command=lambda: [dir_path.set(filedialog.askdirectory()), on_directory_selected()]).pack()

    Label(root, text="Start Month:").pack()
    ttk.Combobox(root, textvariable=start_month_var, values=[str(i) for i in range(1, 13)]).pack()

    Label(root, text="End Month:").pack()
    ttk.Combobox(root, textvariable=end_month_var, values=[str(i) for i in range(1, 13)]).pack()

    Label(root, text="Year:").pack()
    ttk.Combobox(root, textvariable=year_var, values=[str(i) for i in range(2020, 2051)]).pack()

    Label(root, text="Date Format:").pack()
    ttk.Combobox(root, textvariable=date_format_var, values=['MM_YYYY', 'YYYY_MM', 'MMM_YYYY', 'YYYY_MMM']).pack()

    Label(root, text="Detail Position:").pack()
    ttk.Combobox(root, textvariable=detail_position_var, values=['Beginning', 'End']).pack()

    Label(root, text="Additional Detail:").pack()
    Entry(root, textvariable=detail_var).pack()

    preview_list = Listbox(root)
    preview_list.pack()

    update_button = Button(root, text="Update Preview", command=lambda: update_preview(start_month_var.get(), end_month_var.get(), detail_var.get(), preview_list, year_var.get(), date_format_var.get(), detail_position_var.get()), state='disabled')
    update_button.pack()

    confirm_button = Button(root, text="Confirm and Create Folders", command=on_confirm, state='disabled')
    confirm_button.pack()

    clear_button = Button(root, text="Clear", command=clear_entries)
    clear_button.pack()

    quit_button = Button(root, text="Quit", command=root.destroy)
    quit_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
