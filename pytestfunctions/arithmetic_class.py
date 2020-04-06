class ArithmeticClass:
    def add(self, x, y):
        print('Adding two numbers {} & {} '.format(x, y))
        res = x + y
        return res

    def mod(self, x, y):
        print('Mod two numbers {} & {} '.format(x, y))
        res = x % y
        return res

    def product(self, x, y):
        print('Mul two numbers {} & {} '.format(x, y))
        res = x * y
        return res
