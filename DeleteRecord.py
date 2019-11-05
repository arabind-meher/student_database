from tkinter import *
from tkinter import messagebox
import mysql.connector

myDatabase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='********',
    database='test_db'
)


class DeleteRecord:
    def __init__(self, master):
        self.master = master

        master.geometry('350x225')
        master.resizable(0, 0)
        master.title('Student Database')

        Label(master, text='Student Delete', font=('Time New Roman', 24), fg='white', bg='black', padx=10) \
            .pack(fill='x')

        idValue = IntVar()
        Label(master, text='Student ID:', font=('Time New Roman', 16), anchor=W).pack(fill='x')
        Entry(master, textvariable=idValue, font=('Time New Roman', 16)).pack(fill='x')

        nameText = StringVar()
        Label(master, text='Name:', font=('Time New Roman', 16), anchor=W).pack(fill='x')
        Entry(master, textvariable=nameText, font=('Time New Roman', 16)).pack(fill='x')

        Label(master).pack(fill='x')

        def delete_data():
            cursor = myDatabase.cursor()
            command = 'DELETE FROM student WHERE ID = %s AND Name = %s'

            id = idValue.get()
            name = nameText.get()
            data = (id, name)

            print(id, name)

            cursor.execute(command, data)
            myDatabase.commit()

            messagebox.showinfo('Success', 'Data Deleted Successfully')

            print('Success')

        Button(master, text='Delete', command=delete_data, padx=10, pady=10).pack()


def main():
    root = Tk()
    DeleteRecord(root)
    root.mainloop()


if __name__ == '__main__':
    main()
