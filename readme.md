![Новая задача](images/SQLite.jpg)

# **Цель: освоить основные команды языка SQL и использовать их в коде используя SQLite3.**
___
## **Первые пользователи**

_**Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:**_

1. id - целое число, первичный ключ
2. username - текст (не пустой)
3. email - текст (не пустой)
4. age - целое число
5. balance - целое число (не пустой)

Заполните её 10 записями:
1. User1, example1@gmail.com, 10, 1000
2. User2, example2@gmail.com, 20, 1000
3. User3, example3@gmail.com, 30, 1000
...
10. User10, example10@gmail.com, 100, 1000

Обновите balance у каждой 2ой записи начиная с 1ой на 500:
1. User1, example1@gmail.com, 10, 500
2. User2, example2@gmail.com, 20, 1000
3. User3, example3@gmail.com, 30, 500
...
10. User10, example10@gmail.com, 100, 1000

Удалите каждую 3ую запись в таблице начиная с 1ой:
- User2, example2@gmail.com, 20, 1000 
- User3, example3@gmail.com, 30, 500
- User5, example5@gmail.com, 50, 500
...
- User9, example9@gmail.com, 90, 500

Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>