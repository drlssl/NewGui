class test:
    a = 10
    b = True

    def a_plus01(self):
        self.a += 1
        return self.a

    def a_minus01(self):
        self.a -= 1
        return self.a

    def a_cal(self):
        if self.b:
            self.a_plus01()
        else:
            self.a_minus01()
        return self.a


test = test()
res = test.a_cal()
print(res)
