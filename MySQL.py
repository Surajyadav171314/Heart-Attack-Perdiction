import mysql.connector
from tkinter import messagebox

#

def Save_Data_MySql(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R):
    
    try:
        mydb = mysql.connector.connect( host="localhost", 
                                        user="root",
                                        password="admin")
        mycursor = mydb.cursor() 
        print("Connection established")

    except:
        messagebox.showerror("Connection", "Database connection not established: {err}")
    
    try:
        command="create database Heart_Data"
        mycursor.execute(command)

        command="use Heart_Data"
        mycursor.execute(command)

        command = "create table data(user INT AUTO_INCREMENT PRIMARY KEY NOT NULL,Name VARCHAR(50), Date VARCHAR(100), DOB VARCHAR(100), age VARCHAR(100), sex VARCHAR(100), Cp VARCHAR(100),trestbps VARCHAR(100), chol VARCHAR(100),fbs VARCHAR(100),restecg VARCHAR(100), thalach VARCHAR(100), exang VARCHAR(100),oldpeak VARCHAR(100), slope VARCHAR(100), ca VARCHAR(100),thal VARCHAR(100),result VARCHAR(100))"
        mycursor.execute(command)
        
        command = "insert into data(Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, result) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)"
        mycursor.execute(command,(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R))
        mydb.commit()
        mydb.close()
        messagebox.show("Register","New useer added  sucessfully!!")


    except:
        # messagebox.showerror("info",'There is mistake in the above page;')
        mycursor.execute("use Heart_Data")
        mydb=mysql.connector.connect(host="localhost",user='root',password='admin',database='Heart_Data')
        mycursor=mydb.cursor()

        command = "insert into data(Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, result) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)"
        mycursor.execute(command,(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R))
        mydb.commit()
        mydb.close()
        messagebox.show("Register","New useer added  sucessfully!!")


Save_Data_MySql('me unKnown','08/09/2024','1979','44','1','233','1','1','233','233','1','233','1','233.0','0','2','1','0')
