import json
import mysql.connector

connection = None
employee_data_tuple = ()

try:
    with open('./data.txt', 'r') as read_file:
        lines = read_file.readlines()
        print(list(lines))
        employee_data = list(lines)[0]
        print(employee_data)
        dictionary = json.loads(employee_data)
    employee_data = []
    for value in dictionary.values():
        employee_data.append(value)
        employee_data_tuple = tuple(employee_data)
    print(employee_data_tuple)
except:
    print('Issue with file reading')


try:
    connection = mysql.connector.connect(host='10.248.139.139', user='admin', password='test@123')
    insert_query = "INSERT INTO Laptop (id, name, Salary, DeptId) VALUES " + str(employee_data_tuple)
    cursor = connection.cursor()
    cursor.execute(insert_query)
    connection.commit()
except:
    print('Issue with database connection')
finally:
    connection.close()
