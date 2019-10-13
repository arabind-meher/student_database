from tkinter import *
from tkinter import messagebox
import mysql.connector

myDatabase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='arabind123',
    database='test_db'
)


class EntryRecord:
    def __init__(self, master):
        self.master = master

        master.geometry('350x520')
        master.resizable(0, 0)
        master.title('Student Database')

        Label(master, text='Student Entry', font=('Time New Roman', 24), fg='white', bg='black', padx=10) \
            .pack(fill='x')

        idValue = IntVar()
        Label(master, text='Student ID:', font=('Time New Roman', 16), anchor=W).pack(fill='x')
        Entry(master, textvariable=idValue, font=('Time New Roman', 16)).pack(fill='x')

        nameText = StringVar()
        Label(master, text='Name:', font=('Time New Roman', 16), anchor=W).pack(fill='x')
        Entry(master, textvariable=nameText, font=('Time New Roman', 16)).pack(fill='x')

        mark1Value = IntVar()
        Label(master, text='Mark1:', font=('Time New Roman', 16), anchor=W).pack(fill='x')
        Entry(master, textvariable=mark1Value, font=('Time New Roman', 16)).pack(fill='x')

        mark2Value = IntVar()
        Label(master, text='Mark2:', font=('Time New Roman', 16), anchor=W).pack(fill='x')
        Entry(master, textvariable=mark2Value, font=('Time New Roman', 16)).pack(fill='x')

        mark3Value = IntVar()
        Label(master, text='Mark3:', font=('Time New Roman', 16), anchor=W).pack(fill='x')
        Entry(master, textvariable=mark3Value, font=('Time New Roman', 16)).pack(fill='x')

        mark4Value = IntVar()
        Label(master, text='Mark4:', font=('Time New Roman', 16), anchor=W).pack(fill='x')
        Entry(master, textvariable=mark4Value, font=('Time New Roman', 16)).pack(fill='x')

        mark5Value = IntVar()
        Label(master, text='Mark5:', font=('Time New Roman', 16), anchor=W).pack(fill='x')
        Entry(master, textvariable=mark5Value, font=('Time New Roman', 16)).pack(fill='x')

        Label(master).pack(fill='x')

        def submit_data():
            cursor = myDatabase.cursor()
            command = 'INSERT INTO student(ID, Name, Mark1, Mark2, Mark3, Mark4, Mark5, Total, Grade) ' \
                      'values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'

            id = idValue.get()
            name = nameText.get()
            mark1 = mark1Value.get()
            mark2 = mark2Value.get()
            mark3 = mark3Value.get()
            mark4 = mark4Value.get()
            mark5 = mark5Value.get()

            total_mark = mark1 + mark2 + mark3 + mark4 + mark5
            percent = total_mark / 5

            if percent >= 95:
                grade = 'O'
            elif 90 <= percent < 95:
                grade = 'A+'
            elif 85 <= percent < 90:
                grade = 'A'
            elif 75 <= percent < 85:
                grade = 'B+'
            elif 65 <= percent < 75:
                grade = 'B'
            elif 55 <= percent < 65:
                grade = 'C'
            elif 50 <= percent < 55:
                grade = 'P'
            else:
                grade = 'F'

            print(id, name, mark1, mark2, mark3, mark4, mark5, total_mark, grade)

            data = (id, name, mark1, mark2, mark3, mark4, mark5, total_mark, grade)

            cursor.execute(command, data)
            myDatabase.commit()

            messagebox.showinfo('Success', 'Data Entered Successfully')

            print('Success')

        Button(master, text='Submit', command=submit_data, padx=10, pady=10).pack()

        master.mainloop()


def main():
    root = Tk()
    EntryRecord(root)
    root.mainloop()


if __name__ == '__main__':
    main()
