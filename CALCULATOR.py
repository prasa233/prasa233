#Design a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result
#Arithmetic
class Arithmetic:
    def getvals(self):
        self.a=float(input("Enter First value:"))
        self.b=float(input("Enter second value:"))
        self.op=input("Enter Any Arithmetic Operator:")
class Calculator:
    @staticmethod
    def cal(ao):
        match(ao.__dict__['op']):
            case "+":
                print("sum({},{})={}".format(ao.__dict__['a'],ao.__dict__['b'],ao.__dict__['a']+ao.__dict__['b']))
            case "-":
                print("sum({},{})={}".format(ao.__dict__['a'],ao.__dict__['b'],ao.__dict__['a']-ao.__dict__['b']))
            case "*":
                print("mul({},{})={}".format(ao.a,ao.b,ao.a*ao.b))
            case "/":
                print("div({},{})={}".format(ao.a,ao.b, ao.a/ao.b))
            case "//":
                print("div({},{})={}".format(ao.a,ao.b,ao.a//ao.b))
            case "%":
                print("mod({},{})={}".format(ao.a,ao.b , ao.a%ao.b))
            case "**":
                print("pow({},{})={}".format(ao.a,ao.b,ao.a**ao.b))
            case _:
                print("{} is not Arithmetic operator-try again".format(ao.op))
ao=Arithmetic()
while(True):
    try:
        ao.getvals()
        Calculator.cal(ao)
    except ValueError:
        print("Don't enter alnums,strs and symblos--try again")
    else:
        break





