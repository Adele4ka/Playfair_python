import numpy as np
import string


class Playfer:
    def __init__(self, key):
        self.key = key

# шифрование биграмм
    def crypt_b(self, bigram):
        # находим расположение символов биграммы в таблице
        temp1 = np.where(self.key == bigram[0])
        temp2 = np.where(self.key == bigram[1])
        ind1 = [temp1[0][0], temp1[1][0]]
        ind2 = [temp2[0][0], temp2[1][0]]
        if ind1[0] == ind2[0]:  # если равны номера строк
            # сдвигаем на 1 ячейку вправо:
            ind1[1] = (ind1[1] + 1) % 5
            ind2[1] = (ind2[1] + 1) % 5
        elif ind1[1] == ind2[1]:  # если равны номера столбцов
            # сдвигаем на 1 ячейку вниз:
            ind1[0] = (ind1[0] + 1) % 5
            ind2[0] = (ind2[0] + 1) % 5
        else:  # иначе
            # меняем номера столбцов
            t = ind1[1]
            ind1[1] = ind2[1]
            ind2[1] = t
        crypt_bigram = "".join(self.key[ind1[0]][ind1[1]] + self.key[ind2[0]][ind2[1]])
        return crypt_bigram

# шифрование сообщения
    def crypt(self, text):
        # уберем пробелы, буквы 'j' заменим на 'i' и приведем символы к нижнему регистру
        text = ''.join(text.split())
        text = text.lower().replace('j', 'i')
        if len(text) % 2 == 1:
            text += 'x'
        cr_text = ''
        while len(cr_text) < len(text):
            bigram = text[len(cr_text)] + text[len(cr_text) + 1]
            cr_text += self.crypt_b(bigram)
        return cr_text

# дешифрование биграмм
    def decrypt_b(self, bigram):
        temp1 = np.where(self.key == bigram[0])
        temp2 = np.where(self.key == bigram[1])
        ind1 = [temp1[0][0], temp1[1][0]]
        ind2 = [temp2[0][0], temp2[1][0]]
        if ind1[0] == ind2[0]:
            ind1[1] = (ind1[1] - 1 + 5) % 5
            ind2[1] = (ind2[1] - 1 + 5) % 5
        elif ind1[1] == ind2[1]:
            ind1[0] = (ind1[0] - 1 + 5) % 5
            ind2[0] = (ind2[0] - 1 + 5) % 5
        else:
            t = ind1[1]
            ind1[1] = ind2[1]
            ind2[1] = t
        crypt_bigram = "".join(self.key[ind1[0]][ind1[1]] + self.key[ind2[0]][ind2[1]])
        return crypt_bigram

# дешифрование сообщения
    def decrypt(self, text):
        cr_text = ''
        while len(cr_text) < len(text):
            bigram = text[len(cr_text)] + text[len(cr_text) + 1]
            cr_text += self.decrypt_b(bigram)
        return cr_text


# в качестве ключа запишем алфавит а таблицу
# удаляем символ 'j' и приводим к размерности 5х5
key = np.array(list(string.ascii_lowercase.replace('j', ''))).reshape((5, 5))
print("Введите сообщение, которое надо зашифровать:")
text = input()
Pr = Playfer(key)  # создаем объект класса
cr = Pr.crypt(text)  # вызываем метод шифрования текста
print("Зашифрованный текст:")
print(cr)
decr = Pr.decrypt(cr)  # вызываем метод дешифрования текста
print("Расшифрованый текст:")
print(decr)
