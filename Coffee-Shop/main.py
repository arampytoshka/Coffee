from db import DB

db = DB("localhost", "root", "", "test")



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
        grade = int(input('Оцените, работу '+ barista_name + ' от 1 до 5\n'))
        if grade < 1 or grade > 5:
            return barista_grade()
        return grade

    except ValueError:
        print('Я вас не понимаю')
        return barista_grade()


def milk_question():

    milk = str(input('Добавить молоко?\n'))
    if milk == 'да' or milk == 'Да' or milk == 'ДА':
        milk_result = bool(1)
        print(customer_name_current + ', ' + 'ваш напиток готов, кофе ' + str(res_volume) + 'мл ' + 'c молоком')

    elif milk == 'нет' or milk == 'Нет' or milk == 'НЕТ':
        milk_result = bool(0)
        print(customer_name_current + ', ' + 'ваш напиток готов, кофе ' + str(res_volume) + 'мл')

    else:
        print('Я вас не понимаю')
        return milk_question()
    return milk_result


select_stuff = "SELECT * from stuff where position = 1 order by rand() limit 1"
barista_get_data = db.execute_read_query(select_stuff)

for row in barista_get_data:
    barista_id = row[0]
    barista_name = row[1]


print('Милости прошу к нашему шалашу!\n' 'Вас будет обслуживать ' + barista_name)


customer_name_current = input('Как Вас зовут?\n')
print('Приветствую ' + customer_name_current + '!')
insert_customer = f"INSERT INTO customers (name) values ('{customer_name_current}')"
customer_id = db.execute_query(insert_customer)

customer_name = customer_name_current

insert_orders_barista_customer = f"INSERT INTO orders (stuff_id, customer_id) values ('{barista_id}', '{customer_id}')"
order_id = db.execute_query(insert_orders_barista_customer)

res_volume = volume_question()

print('Ваш объем ' + str(res_volume))

insert_orders_volume = f"UPDATE orders set volume = {res_volume} where id = {order_id}"
update_order = db.execute_query(insert_orders_volume)

milk_result = milk_question()


insert_orders_milk = f"UPDATE orders set is_milk = {milk_result} where id = {order_id}"
update_order = db.execute_query(insert_orders_milk)



res_grade = barista_grade()
print('Ваш оценка ' + barista_name + ' ' + '=' + ' ' + str(res_grade))
print('Всего хорошего!')



insert_orders_grade = f"UPDATE orders set grade = {res_grade} where id = {order_id}"
update_order = db.execute_query(insert_orders_grade)