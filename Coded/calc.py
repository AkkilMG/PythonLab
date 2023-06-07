

class Calc:
    def Add(self, a, b):
        print(f"Sum: {a+b}")

    def Sub(self, a, b):
        print(f"Sum: {a-b}")

    def Multi(self, a, b):
        print(f"Sum: {a*b}")

    def Division(self, a, b):
        print(f"Quotient: {a/b}")

if __name__ == "__main__":
    calc = Calc()
    a = int(input("Enter the a: "))
    b = int(input("Enter the b: "))
    calc.Add(a,b)
    calc.Sub(a,b)
    calc.Multi(a,b)
    calc.Division(a,b)