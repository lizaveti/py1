# TODO  Напишите функцию count_letters
def count_letters(text):
    number_of_letters = 0
    text = text.lower()

    count_dict = {}
    for char in text:
        if char.isalpha():
            number_of_letters += 1
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    return count_dict, number_of_letters



# TODO Напишите функцию calculate_frequency
def calculate_frequency(count_dict, number_of_letters):

    for key, value in count_dict.items():
        count_dict[key] = round(value / number_of_letters, 2)

    return count_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
count_dict, number_of_letters = count_letters(main_str)
letters_frequency = calculate_frequency(count_dict, number_of_letters)


for key, value in letters_frequency.items():
    print (key + ': ' + '%.2f' % value)
