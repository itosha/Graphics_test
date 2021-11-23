import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as spSt
X = [[], [], [], []]
Y = [[], [], [], []]
with open("table1_2_5.txt", 'r') as f:
    for i in range(1):
        """причесываем данные из файла
        я разделяю в файле числа не пробелами а табуляциями, тк так по умолчанию копируется из EXcel
        так же в файле надо чтобы дробная часть отделялась точкой
        """
        x = list((f.readline().split('\t')))
        y = list((f.readline()).split('\t'))
        #errx = list((f.readline().split('\t')))
        #erry = list((f.readline()).split('\t'))
        y = y[:-1]
        x = x[:-1]
        #print(x)
        for j in range(len(x)):
            x[j] = float(x[j])
            y[j] = float(y[j])
            #errx[j] = float(errx[j])
            #erry[j] = float(erry[j])
        X[i] = x
        #print(x)
        Y[i] = y
        """само построение графика"""
        resalt = spSt.linregress(x, y)
        print(resalt)
        z, d = np.polyfit(x, y, 1, cov=True)
        k = float(z[0])
        b = float(z[1])
        #print(d)
        print("Коэфициент углового наклона и сдвиг по Y: ", k, b)
        s = list(range(len(x)))
        #print(x)
        for t in range(len(x)):
            s[t] = k * x[t] + b
        plt.figure()
        #print(x)
        #plt.scatter(x, y)
        """кресты ошибок. к сожалению не знаю как сделать для разных точек разные кресты"""
        plt.errorbar(x, y, fmt='ro', xerr=0, yerr=0.001)
        plt.plot(x, s)
        """подписываем оси"""
        plt.xlabel(r'$M,H*m$', fontsize=16)
        plt.ylabel(r'$W,1/c$', fontsize=16)
        plt.grid(True)
#print(X)
"""регулируем масштаб вручную если не хотим пользоваться автоматическим"""
plt.xticks(np.arange(0.1, 0.33, 0.01))
plt.yticks(np.arange(0.05, 0.17, 0.01))
plt.show()