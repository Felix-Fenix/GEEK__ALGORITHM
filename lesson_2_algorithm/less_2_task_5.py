"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и
заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар
"код-символ" в каждой строке.

"""
a = 32
b = 127
def recur(a,b):
        if a == b:
            return print("%4d - %s" % (b, chr(b)))
        if a % 10 == 0:
            print()
        return str(print("%4d - %s" % (a, chr(a)), end=' '))+ str(recur(a + 1, b))

recur(a,b)

# for i in range(32,128):
#     print("%4d= %s" % (i,chr(i)), end='')
#     if i % 10 == 0:print()