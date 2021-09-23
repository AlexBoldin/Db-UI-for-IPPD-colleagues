import pymysql
import pandas as pd

data = pd.read_excel("Solubility_Data.xlsx")
data = data.fillna(0)

try:
    connection = pymysql.connect(
      host="localhost",
      user="root",
      password="1235"
    )
    cursor = connection.cursor()
    cursor.execute('DROP DATABASE IF EXISTS book2')
    connection.commit()
    cursor.execute('CREATE DATABASE book2')
    connection.commit()
    cursor.execute('USE book2')
    connection.commit()
    
    sql = """CREATE TABLE book_details2 (
             API varchar(3000),
             PF varchar(3000),
             PEG_600 DECIMAL(19,2), 
             PEG_400 DECIMAL(19,2),
             PEG_300 DECIMAL(19,2), 
             PEG_200 DECIMAL(19,2),
             WATER DECIMAL(19,2), 
             ETHANOL DECIMAL(19,2),
             NMP DECIMAL(19,2), 
             DMSO DECIMAL(19,2),
             PG DECIMAL(19,2), 
             EXP_VAL DECIMAL(19,8),
             THEOR_VAL DECIMAL(19,8))"""
    
    cursor.execute(sql)
    connection.commit()
    cols = "`,`".join([str(i) for i in data.columns.tolist()])

# Insert DataFrame recrds one by one.
    for i,row in data.iterrows():
        sql2 = "INSERT INTO `book_details2` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
        cursor.execute(sql2, tuple(row))
    
        # the connection is not autocommitted by default, so we must commit to save our changes
    connection.commit()
    
    
    sql3 = "SELECT * FROM `book_details2`"
    cursor.execute(sql3)


finally:
    
    connection.commit()
    connection.close()
