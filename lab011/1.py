import psycopg2
import csv

def check_number(phone):
    phone = str(phone)
    if phone[:2] == '87' or phone[:2] == '+7':
        return True
    else:
        return False

def limit(cursor):
    try:
        print('Сколько пользователей вы хотите вывести?')
        x = int(input())
        cursor.execute('SELECT name, phone FROM contacts LIMIT %s', (x,))
        records = cursor.fetchall()

        if records:
            print('Результаты:')
            for record in records:
                print(record)
        else:
            print('Нет данных для отображения.')
    except ValueError:
        print('Ошибка: Введите корректное число.')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

def multiadd(conn, cursor):
    try:
        cursor.execute('SELECT * FROM contacts')
        records = cursor.fetchall()
        not_cor = []
        with open('C:\\Users\\HP\\Desktop\\CPP\\pp2\\lab11\\sample.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i in csv_reader:
                check = True
                for j in records:
                    if i[1] == j[1]:
                        check = False
                        break
                if not check_number(i[0]):
                    not_cor.append(i)
                    check = False
                if check:
                    cursor.execute('INSERT INTO contacts(name, phone) VALUES(%s, %s)', (i[0], i[1]))
                    conn.commit()
                else:
                    cursor.execute('UPDATE contacts SET phone = %s WHERE name = %s', (i[1], i[0]))
                    conn.commit()

        if not_cor:
            print('Неверные данные:')
            print(not_cor)
    except Exception as e:
        print(f'Произошла ошибка: {e}')

def pattern(cursor):
    try:
        print('Введите начало шаблона имени')
        y = input()
        cursor.execute("SELECT * FROM contacts WHERE name LIKE %s", (y + '%',))
        records = cursor.fetchall()

        if records:
            print('Все совпадения:')
            for record in records:
                print(record)
        else:
            print('Совпадений не найдено')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

def delete(conn, cursor):
    try:
        print('Удаление по номеру 1, по имени 2')
        x = input()
        if x == '1':
            phone = int(input('Введите номер телефона: '))
            cursor.execute('DELETE FROM contacts WHERE phone = %s', (phone,))
        elif x == '2':
            name = input('Введите имя: ')
            cursor.execute('DELETE FROM contacts WHERE name = %s', (name,))
        else:
            print('Неверный выбор.')
            return
        conn.commit()
        print("Удаление произошло успешно")
    except Exception as e:
        print(f'Произошла ошибка: {e}')

def update(conn, cursor):
    try:
        print('Введите ID контакта, который хотите обновить')
        user_id = int(input())

        print('Что вы хотите обновить? (имя, фамилия, номер)')
        field = input()

        print('Введите новое значение')
        new_value = input()

        if field == 'имя':
            cursor.execute('UPDATE contacts SET name = %s WHERE id = %s', (new_value, user_id))
        elif field == 'фамилия':
            cursor.execute('UPDATE contacts SET last_name = %s WHERE id = %s', (new_value, user_id))
        elif field == 'номер':
            cursor.execute('UPDATE contacts SET phone = %s WHERE id = %s', (new_value, user_id))
        else:
            print('Неверное поле для обновления.')
            return

        conn.commit()
        print('УСПЕШНО!')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

def show(cursor):
    try:
        print('Только номера:')
        cursor.execute('SELECT phone FROM contacts')
        phones = cursor.fetchall()
        print(phones)

        print('Имя и номер:')
        cursor.execute('SELECT id, name, last_name, phone FROM contacts')
        contacts = cursor.fetchall()
        print(contacts)
    except Exception as e:
        print(f'Произошла ошибка: {e}')

def add(conn, cursor):
    try:
        print('Введите имя и номер пользователя (например: Турар 8923456789):')
        z = input().split()
        if len(z) != 2:
            print('Ошибка: Введите имя и номер через пробел.')
            return

        name = z[0]
        try:
            phone = int(z[1])
        except ValueError:
            print('Ошибка: Номер телефона должен быть числом.')
            return

        cursor.execute('SELECT phone FROM contacts WHERE name = %s', (name,))
        existing = cursor.fetchone()

        if existing:
            cursor.execute('UPDATE contacts SET phone = %s WHERE name = %s', (phone, name))
        else:
            cursor.execute('INSERT INTO contacts(name, phone) VALUES(%s, %s)', (name, phone))

        conn.commit()
        print("УСПЕШНО!")
    except Exception as e:
        print(f'Произошла ошибка: {e}')

# Database connection
conn = psycopg2.connect("dbname=postgres user=postgres password=96066970 port=3456")
cursor = conn.cursor()

# Main loop
while True:
    choose = input("Выберите что вы хотите сделать:\n1:Добавить контакт\n2:Удалить контакт\n3:Показать контакты\n4:Обновить контакт\n5:Шаблон\n6:multiadd\n7:limit\nexit:Выход\n")
    if choose == '1':
        add(conn, cursor)
    elif choose == '2':
        delete(conn, cursor)
    elif choose == '3':
        show(cursor)
    elif choose == '4':
        update(conn, cursor)
    elif choose == '5':
        pattern(cursor)
    elif choose == '6':
        multiadd(conn, cursor)
    elif choose == '7':
        limit(cursor)
    elif choose == 'exit':
        break
    else:
        print('Неверный выбор. Попробуйте снова.')

cursor.close()
conn.close()