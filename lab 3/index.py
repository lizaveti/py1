# TODO Напишите функцию для поиска индекса товара
def find_item(items, item):
    for i in range(len(items)):
        if items[i] == item:
            return i
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for item in ['банан', 'груша', 'персик']:
    index_item = find_item(items=items_list, item=item)
    if index_item is not None:
        print(f"Первое вхождение товара '{item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{item}' не найден в списке.")
