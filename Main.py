from tkinter import *

import EntryRecord as Entry
import DeleteRecord as Delete
import ViewRecord as View


def entry_record():
    root.destroy()
    Entry.main()


def delete_record():
    root.destroy()
    Delete.main()


def view_record():
    root.destroy()
    View.main()


if __name__ == '__main__':
    root = Tk()
    root.geometry('435x120')
    root.resizable(0, 0)
    root.title('Student Database')

    Label(root, text='Welcome to Student Database', font=('Time New Roman', 24), fg='white', bg='black') \
        .grid(row=0, column=0, columnspan=3)

    Label(root).grid(row=1, column=0, columnspan=3)

    Button(root, text='Entry Record', command=entry_record, pady=10).grid(row=2, column=0)

    Button(root, text='Delete Record', command=delete_record, pady=10).grid(row=2, column=1)

    Button(root, text='View Record', command=view_record, pady=10).grid(row=2, column=2)

    root.mainloop()
