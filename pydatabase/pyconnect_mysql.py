import mysql.connector

try:
    connection = mysql.connector.connect(host = '10.248.139.139', user='admin' , password = 'test@123')
    insert_query = "INSERT INTO Laptop (id, name, Salary, DeptId) VALUES (9001, 'John', '150000', '45')"
    cursor = connection.cursor()
    cursor.execute(insert_query)
    connection.commit()
except:
    print('Something went wrong!')
finally:
    connection.close()






