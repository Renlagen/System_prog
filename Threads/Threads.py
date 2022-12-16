from threading import Thread


def Prog1(file1, age):
    with open(file1, 'w') as f1:
        for i in range(age):
            if age > 18 and age != 33:
                f1.write('Я взрослый\n')
            elif age == 33:
                f1.write('Меня зовут Кира Йошикаге. Мне 33 года. Мой дом находится в северо-восточной части Морио, где расположены все виллы. Я не женат. Я не курю, но иногда выпиваю. Я ложусь спать в 11 вечера, и убеждаюсь, что я получаю ровно восемь часов сна, несмотря ни на что. \n')
            else:
                f1.write('Я еще дитя\n')


thread1 = Thread(target=Prog1, args=('f1.txt', 14,))
thread2 = Thread(target=Prog1, args=('f2.txt', 20,))
thread3 = Thread(target=Prog1, args=('f3.txt', 33,))

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()