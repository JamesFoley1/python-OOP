class MathDojo():
    def __init__(self):
        self.result = 0
    
    def add(self, *args):
        for i in range(len(args)): 
            self.result += args[i]
            print("Result:", self.result)
        return self

    def subtract(self, *args):
        for i in range(len(args)): 
            self.result -= args[i]
            print("Result:", self.result)
        return self


md = MathDojo()
md.add(2).add(2,5,1).subtract(3,2)
