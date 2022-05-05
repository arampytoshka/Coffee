import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
connection = create_connection("localhost", "root", "", "test")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def volume_question():
    try:
        volume = int(input('Какой у вас объем стакана?\n'))
        if volume < 200:
            print('Объем измеряется в миллилитрах и не может быть меньше 200')
            return volume_question()
        return volume

    except ValueError:
        print('Я вас не понимаю')
        return volume_question()



def barista_grade():
    try:
        grade = int(input('Оцените, работу '  + barista_name + ' от 1 до 5\n'))
        if grade < 1 or grade > 5:
            return barista_grade()
        return grade

    except ValueError:
        print('Я вас не понимаю')
        return barista_grade()


def milk_question():
    global milk_result
    milk = str(input('Добавить молоко?\n'))
    if milk == 'да' or milk == 'Да' or milk == 'ДА':
        milk_result = bool(1)
        print(customer_name_current + ', ' + 'ваш напиток готов, кофе ' + str(res_volume) + 'мл ' + 'c молоком')

    elif milk == 'нет' or milk == 'Нет' or milk == 'НЕТ':
        milk_result = bool(0)
        print(customer_name_current + ', ' + 'ваш напиток готов, кофе ' + str(res_volume) + 'мл')

    else:
        print('Я вас не понимаю')
        milk_question()






select_stuff = "SELECT * from stuff where position = 1 order by rand() limit 1"
barista_get_data = execute_read_query(connection, select_stuff)

for row in barista_get_data:
    barista_id = row[0]
    barista_name = row[1]


print('Милости прошу к нашему шалашу!\n' 'Вас будет обслуживать ' + barista_name)


customer_name_current = input('Как Вас зовут?\n')
print('Приветствую ' + customer_name_current + '!')

insert_customers = f"INSERT INTO customers (name) values ('{customer_name_current}')"
new_customer = execute_query(connection, insert_customers)

select_customer = f"SELECT * from customers where name = ('{customer_name_current}') order by id"
customer_get_data = execute_read_query(connection, select_customer)



for row in customer_get_data:
    customer_id = row[0]
    customer_name = row[1]
# print(customer_id)
# print(customer_name)

insert_orders_barista_customer = f"INSERT INTO orders (stuff_id, customer_id) values ('{barista_id}', '{customer_id}')"
new_order = execute_query(connection, insert_orders_barista_customer)

select_order = f"SELECT * from orders order by id"
order_get_data = execute_read_query(connection, select_order)

for row in order_get_data:
    order_id = row[0]
# print(order_id)

res_volume = volume_question()

print('Ваш объем ' + str(res_volume))

insert_orders_volume = f"UPDATE orders set volume = {res_volume} where id = {order_id}"
update_order = execute_query(connection, insert_orders_volume)

milk_question()
# print(milk_result)

insert_orders_milk = f"UPDATE orders set is_milk = {milk_result} where id = {order_id}"
update_order = execute_query(connection, insert_orders_milk)



res_grade = barista_grade()
print('Ваш оценка ' + barista_name + ' ' + '=' + ' ' + str(res_grade))
print('Всего хорошего!')



insert_orders_grade = f"UPDATE orders set grade = {res_grade} where id = {order_id}"
update_order = execute_query(connection, insert_orders_grade)