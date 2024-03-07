# В скобках {} отмечается тип данных 'словарь'.
# Элементы помещаются парами, пара отмечается через :, а следующая пара через запятую.
# В [] отмечается список.

def sk(strok):
    skob = {')': '(', ']': '[', '}': '{'}
    stek_skob, stek_ind = [], []
    # Обозначаем счетчик, чтобы можно было вывести номер элемента на котором будет обнаружена ошибка.
    # Ошибкой считается, если у закрывающей до этого не было открывающей
    # и если открывающая закрылась не своей скобкой - (}, [) итд.
    c = 1
    inp = list(strok)
    # Проверяем
    for i in inp:
        if i in skob.values():
            stek_skob.append(i)
            stek_ind.append(c)
            c += 1
        elif i in skob.keys():
            if len(stek_skob) != 0:
                # Когда передается индекс, метод .pop() удаляет элемент по индексу, а также возвращает то же самое.
                if stek_skob.pop() == skob[i]:
                    stek_ind.pop()
                    c += 1
                else:
                    return c
            else:
                return c
        else:
            c += 1
    return 'Success' if len(stek_skob) == 0 else stek_ind[-1]


print(sk(input()))
