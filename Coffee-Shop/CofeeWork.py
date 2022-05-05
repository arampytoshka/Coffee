from db import DB
db_work = DB("localhost", "root", "", "test")
class CoffeeWork:
    volume = None
    grade = None
    barista_name = None
    customer_name_current = None
    is_milk = None
    def __volume_question(self):
        try:
            self.volume = int(input('Какой у вас объем стакана?\n'))
            if self.volume < 200:
                print('Объем измеряется в миллилитрах и не может быть меньше 200')
                return self.__volume_question()
        except ValueError:
            print('Я вас не понимаю')
            return self.__volume_question()

    def __barista_grade(self):
        try:
            self.grade = int(input('Оцените, работу ' + self.barista_name + ' от 1 до 5\n'))
            if self.grade < 1 or self.grade > 5:
                return self.__barista_grade()

        except ValueError:
            print('Я вас не понимаю')
            return self.__barista_grade()

    def __milk_question(self):

        milk = str(input('Добавить молоко?\n'))
        if milk == 'да' or milk == 'Да' or milk == 'ДА':
            self.is_milk = bool(1)
            print(self.customer_name_current + ', ' + 'ваш напиток готов, кофе ' + str(self.volume) + 'мл ' + 'c молоком')
        elif milk == 'нет' or milk == 'Нет' or milk == 'НЕТ':
            self.is_milk = bool(0)
            print(self.customer_name_current + ', ' + 'ваш напиток готов, кофе ' + str(self.volume) + 'мл')

        else:
            print('Я вас не понимаю')
            return self.__milk_question()

    def work(self):
        select_stuff = "SELECT * from stuff where position = 1 order by rand() limit 1"
        barista_get_data = db_work.execute_read_query(select_stuff)
        for row in barista_get_data:
            barista_id = row[0]
            self.barista_name = row[1]
        print('Милости прошу к нашему шалашу!\n' 'Вас будет обслуживать ' + self.barista_name)

        self.customer_name_current = input('Как Вас зовут?\n')
        print('Приветствую ' + self.customer_name_current + '!')
        insert_customer = f"INSERT INTO customers (name) values ('{self.customer_name_current}')"
        customer_id = db_work.execute_query(insert_customer)

        insert_orders_barista_customer = f"INSERT INTO orders (stuff_id, customer_id) values ('{barista_id}', '{customer_id}')"
        order_id = db_work.execute_query(insert_orders_barista_customer)

        self.__volume_question()
        insert_orders_volume = f"UPDATE orders set volume = {self.volume} where id = {order_id}"
        update_order = db_work.execute_query(insert_orders_volume)

        self.__milk_question()
        insert_orders_milk = f"UPDATE orders set is_milk = {self.is_milk} where id = {order_id}"
        update_order = db_work.execute_query(insert_orders_milk)

        self.__barista_grade()
        print('Ваш оценка ' + self.barista_name + ' ' + '=' + ' ' + str(self.grade))
        print('Всего хорошего!')

        insert_orders_grade = f"UPDATE orders set grade = {self.grade} where id = {order_id}"
        update_order = db_work.execute_query(insert_orders_grade)

test = CoffeeWork()
test.work()