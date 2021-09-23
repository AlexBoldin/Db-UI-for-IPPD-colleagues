import pymysql
from tkinter import *
import tkinter.ttk as ttk

#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("1200x700")
    #setting title for window
    display_screen.title("IPPD Solubility SQL Database alpha")
    global tree
    global SEARCH
    SEARCH = StringVar()
    #creating frame
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(display_screen, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="IPPD Solubility SQL Database alpha", \
                     font=('verdana', 18), width=600,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('verdana', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)

    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="View All", command=DisplayData)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("API", "PF", "PEG_600", \
    "PEG_400","PEG_300","PEG_200", "WATER", "ETHANOL", "NMP", "DMSO", \
    "PG", "EXP_VAL", "THEOR_VAL"),
                        selectmode="extended", height=100, \
                            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('API', text="API", anchor=W)
    tree.heading('PF', text="PF", anchor=W)
    tree.heading('PEG_600', text="PEG_600", anchor=W)
    tree.heading('PEG_400', text="PEG_400", anchor=W)
    tree.heading('PEG_300', text="PEG_300", anchor=W)
    tree.heading('PEG_200', text="PEG_200", anchor=W)
    tree.heading('WATER', text="WATER", anchor=W)
    tree.heading('ETHANOL', text="ETHANOL", anchor=W)    
    tree.heading('NMP', text="NMP", anchor=W)
    tree.heading('DMSO', text="DMSO", anchor=W)
    tree.heading('PG', text="PG", anchor=W)
    tree.heading('EXP_VAL', text="EXP_VAL", anchor=W)
    tree.heading('THEOR_VAL', text="THEOR_VAL", anchor=W)
    
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=60)
    tree.column('#4', stretch=NO, minwidth=0, width=60)
    tree.column('#5', stretch=NO, minwidth=0, width=60)
    tree.column('#6', stretch=NO, minwidth=0, width=60)
    tree.column('#7', stretch=NO, minwidth=0, width=60)
    tree.column('#8', stretch=NO, minwidth=0, width=80)
    tree.column('#9', stretch=NO, minwidth=0, width=60)
    tree.column('#10', stretch=NO, minwidth=0, width=60)
    tree.column('#11', stretch=NO, minwidth=0, width=40)
    tree.column('#12', stretch=NO, minwidth=0, width=100)
    tree.column('#13', stretch=NO, minwidth=0, width=100)
    
    tree.pack()
    DisplayData()
#function to search data
def SearchRecord():
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #open database
        #db = sqlite3.connect('Data.db')
        
        try:
            connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1235",
            db='book2'
            )
            cursor = connection.cursor()
        
            cursor.execute("SELECT * FROM book_details2 WHERE API LIKE %s", \
                           ('%' + str(SEARCH.get()) + '%',))
            fetch = cursor.fetchall()    
                
        #loop for displaying all records into GUI
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            
               
        finally:    
            connection.commit()
            connection.close()
                
#defining function to access data from SQLite database
def DisplayData():
    #clear current data
    tree.delete(*tree.get_children())
    # open databse
    # db = sqlite3.connect('Data.db')
    try:
        connection = pymysql.connect(
        host="localhost",
        user="root",
        password="1235",
        db='book2'
        )
        cursor = connection.cursor()

        sql3 = "SELECT * FROM `book_details2`"
        cursor.execute(sql3)
        fetch = cursor.fetchall()
    #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        
        # for data in fetch:
        #     tree.insert('', 'end', values=(data))        
        
    finally:    
        connection.commit()
        connection.close()

#calling function
DisplayForm()
if __name__=='__main__':
#Running Application
 mainloop()
