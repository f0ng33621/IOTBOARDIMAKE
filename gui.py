from tkinter import *
from turtle import bgcolor 
import socket




def client_program():
    host = '192.168.31.206'  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

# def CloseStair():
#     Label_Test.config(text = "บันไดกำลังถูกพับเก็บเข้าตำแหน่ง")
#     Label_Test3 = Label(text='ขอย้ำบันไดกำลังถูกพับเก็บเข้าตำแหน่ง',width=40)
#     Label_Test3.pack()

    
# app = Tk()
# app.option_add('*font',"Times", "90")
# app.title("WARNING")
# app.geometry("500x500")
# frame = Frame(app)
# frame.config(background="Grey")
# frame.place(width=500,height=500,x=0,y=0)
# Label_Test = Label(text='มีคนตกลงไปจากชานชาลา')
# Label_Test.config(bg="red")
# Label_Test.pack()
# Button_Test = Button(text='ช่วยเหลือแล้ว',command=CloseStair)
# Button_Test.pack()
# Label_Test2 = Label(text='อย่ากดปุ่มช่วยเหลือแล้วจนกว่าการช่วยเหลือจะเสร็จสิ้น',width=50,bg='yellow')
# Label_Test2.pack()
# app.mainloop() 