import BD_SQLite3 as bd
import logging
NAME_BD = 'not_telegram.db'     # имя БД

def main():
    bd.create_table(NAME_BD)    # создадим БД

    # формируем списки для вставки, обновления и удаления записей в БД
    lst_insert = [(f'User{str(i)}', f'example{str(i)}@gmail.com', i*10, 1000) for i in range(1, 11)]
    lst_update = [(500, f'User{str(i)}') for i in range(1, 11, 2)]
    lst_delete = [(f'User{str(i)}',) for i in range(1, 11, 3)]

    bd.insert_multiple_lines(NAME_BD, lst_insert)       # вставили записи в БД из списка
    bd.update_multiple_lines(NAME_BD, lst_update)       # обновили записи в БД из списка
    bd.delete_multiple_lines(NAME_BD, lst_delete)       # удалили записи из БД по списку

    result = bd.select_all_where(NAME_BD, 60)      # сделали выборку из БД, где возраст не равен 60
    for i in range(len(result)):                        # вывели строки из списка на печать
        print(result[i])

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w", encoding='utf-8',
                        format="%(asctime)s %(levelname)s %(message)s")
    main()



