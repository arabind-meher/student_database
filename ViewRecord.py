from tkinter import *
import mysql.connector

myDatabase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='arabind123',
    database='test_db'
)


def display_record(data):
    show = Tk()
    show.geometry('245x400')
    show.resizable(0, 0)
    show.title('Student Database')

    Label(show, text='Student Record', font=('Time New Roman', 24), fg='white', bg='black', padx=10) \
        .grid(row=0, column=0, columnspan=2)

    Label(show, text='Student ID:', font=('Time New Roman', 16), anchor=W).grid(row=1, column=0)
    Label(show, text=data[0], font=('Time New Roman', 16)).grid(row=1, column=1)

    Label(show, text='Name:', font=('Time New Roman', 16), anchor=W).grid(row=2, column=0)
    Label(show, text=data[1], font=('Time New Roman', 16)).grid(row=2, column=1)

    Label(show, text='Mark1:', font=('Time New Roman', 16), anchor=W).grid(row=3, column=0)
    Label(show, text=data[2], font=('Time New Roman', 16)).grid(row=3, column=1)

    Label(show, text='Mark2:', font=('Time New Roman', 16), anchor=W).grid(row=4, column=0)
    Label(show, text=data[3], font=('Time New Roman', 16)).grid(row=4, column=1)

    Label(show, text='Mark3:', font=('Time New Roman', 16), anchor=W).grid(row=5, column=0)
    Label(show, text=data[4], font=('Time New Roman', 16)).grid(row=5, column=1)

    Label(show, text='Mark4:', font=('Time New Roman', 16), anchor=W).grid(row=6, column=0)
    Label(show, text=data[5], font=('Time New Roman', 16)).grid(row=6, column=1)

    Label(show, text='Mark5:', font=('Time New Roman', 16), anchor=W).grid(row=7, column=0)
    Label(show, text=data[6], font=('Time New Roman', 16)).grid(row=7, column=1)

    Label(show, text='Total:', font=('Time New Roman', 16), anchor=W).grid(row=8, column=0)
    Label(show, text=data[7], font=('Time New Roman', 16)).grid(row=8, column=1)

    Label(show, text='Grade:', font=('Time New Roman', 16), anchor=W).grid(row=9, column=0)
    Label(show, text=data[8], font=('Time New Roman', 16)).grid(row=9, column=1)

    Label(show).grid(row=10, column=0)

    def close_record():
        show.destroy()

    Button(show, text='Close', command=close_record, padx=10, pady=10).grid(row=11, column=0, columnspan=2)


class ViewRecord:
    def __init__(self, master):
        self.master = master

        master.geometry('350x225')
        master.resizable(0, 0)
        master.title('Student Database')

        Label(master, text='Student Record', font=('Time New Roman', 24), fg='white', bg='black', padx=10) \
            .pack(fill='x')

        idValue = IntVar()
        Label(master, text='Student ID:', font=('Time New Roman', 16), anchor=W).pack(fill='x')
        Entry(master, textvariable=idValue, font=('Time New Roman', 16)).pack(fill='x')

        nameText = StringVar()
        Label(master, text='Name:', font=('Time New Roman', 16), anchor=W).pack(fill='x')
        Entry(master, textvariable=nameText, font=('Time New Roman', 16)).pack(fill='x')

        Label(master).pack(fill='x')

        def get_data():
            cursor = myDatabase.cursor()
            command = 'SELECT * FROM student WHERE ID = %s AND Name = %s'

            id = idValue.get()
            name = nameText.get()
            data = (id, name)

            cursor.execute(command, data)
            data = cursor.fetchall()

            display_record(data[0])

            print('ID = ', data[0][0])
            print('Name = ', data[0][1])
            print('Mark1 = ', data[0][2])
            print('Mark2 = ', data[0][3])
            print('Mark3 = ', data[0][4])
            print('Mark4 = ', data[0][5])
            print('Mark5 = ', data[0][6])
            print('Total = ', data[0][7])
            print('Grade = ', data[0][8])

            print('Success')

        Button(master, text='Show', command=get_data, padx=10, pady=10).pack()


def main():
    root = Tk()
    ViewRecord(root)
    root.mainloop()


if __name__ == '__main__':
    main()
