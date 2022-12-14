import numpy as np


class Lagrange:

    def __init__(self):
        self.y = []
        self.a = []
        self.x = []

    def read_file(self, string):
        f = open(string, 'r')
        while True:
            input_str = f.readline()
            if input_str == '':
                break
            arr = input_str.split(" ")
            self.x.append(float(arr[0]))
            self.y.append(float(arr[1]))

        f.close()

    def hoocne_multiply(self, arr):
        b = [1, -arr[0]]
        k = 1
        while k < len(arr):
            b.append(0)
            self.a = [b[0]]  # an = bn
            c = arr[k]
            for i in range(1, len(b)):
                a_k = b[i] - b[i - 1] * c  # a_k = b_k - b_(k + 1) * c
                self.a.append(a_k)
            b = self.a.copy()
            k += 1
        else:
            self.a = b.copy()
        return self.a

    def hoocne_divive(self, arr, c):
        b = [arr[0]]
        for i in range(1, len(arr)):
            b_k = arr[i] + b[i - 1] * c  # b_k = a_k + b_k-1 * c
            b.append(float(b_k))
        return b

    def Degf_k(self, arr, k, c):
        factorial = 1
        for i in range(1, k + 1):
            arr = self.hoocne_divive(arr, c)
            arr.pop() # lay dao ham nen bo gia tri cuoi di
            factorial *= i
        res = self.hoocne_divive(arr, c).pop()  #lay gia tri tai c
        return factorial * res

    def D_i(self, i):
        multi = 1
        for k in range(len(self.x)):
            if k != i:
                multi *= (self.x[i] - self.x[k])
        return multi

    def lagrange(self):
        w = self.hoocne_multiply(self.x)
        summary = np.zeros(len(w))
        for i in range(len(self.x)):
            temp_arr = self.hoocne_divive(w, self.x[i])
            y_D_i = self.y[i] / self.D_i(i)
            temp_arr = [temp_arr[k] * y_D_i for k in range(len(temp_arr))]
            summary = [summary[j] + temp_arr[j] for j in range(len(temp_arr))]
        summary.pop()
        summary = [round(summary[i]) for i in range(len(summary))]
        return summary

    def f_lagrange(self, arr, x):
        return self.hoocne_divive(arr, x).pop()

    def run(self):
        self.read_file("input.txt")
        # print(self.lagrange())
        print(self.Degf_k(self.lagrange(), 3, 2.7))
        # print(self.f_lagrange(self.lagrange(), 2))


if __name__ == "__main__":
    bt = Lagrange()
    bt.run()
