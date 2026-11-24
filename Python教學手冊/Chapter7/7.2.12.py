class Factor:
    factor_list = [2, 3, 6, 8]

    def __init__(self, N):
        print(f"初始化factor_list：{self.factor_list}")
        self.num = N

    def find_factors(self):
        a = []
        for i in range(0, len(self.factor_list)):
            if self.num % self.factor_list[i] == 0:
                a.append(self.factor_list[i])
        return a

    @classmethod
    def add_factor(cls, lst):
        for i in lst:
            if not i in Factor.factor_list:
                Factor.factor_list.append(i)

    @classmethod
    def show_factor_list(cls):
        print(f"{cls.factor_list}")

    @classmethod
    def remove_factor(cls, lst):
        for i in lst:
            if i in cls.factor_list:
                cls.factor_list.remove(i)

    @staticmethod
    def is_factor(num, n):
        if num % n == 0:
            return True
        else:
            return False


f0 = Factor(12)
print(f0.find_factors())
Factor.add_factor([4, 6, 9])
Factor.show_factor_list()
Factor.remove_factor([3, 8])
Factor.show_factor_list()
print(Factor.is_factor(15, 3))
print(Factor.is_factor(15, 4))
