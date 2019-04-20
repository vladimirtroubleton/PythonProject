import codecs
class writer:
    def write(text):
        f1=open('data.txt','a')
        f1.write('\n'+text)
        f1.close
class reader:
    def read():
        f1=open('data.txt','r')
        line=f1.read()
        print("Текст-")
        print(line)
        f1.close
    def clear():
        f1=open('data.txt','w')
        f1.truncate()
lock=0
while lock!=55:

    print("Итак выберите что вы хотите сделать 1- прочитать файл 2- записать ваши данные 3-очистка файла")
    try:
        num=int(input())
    except:
        print("Вы ошиблись")
    if num==1:
        reader.read()
    elif num==2:
        print("Итак пишите")
        text=input()
        writer.write(text)
    elif num==3:
        print("Файл будет очищен")
        reader.clear()
    else:
        print("Ну такого еще нет")
    print("Введите 55 для выхода или любое другое число для продолжения работы")
    lock=int(input())
