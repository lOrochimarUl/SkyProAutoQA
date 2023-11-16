class Smartpone:

    def __init__(self, mark, model, number) -> None:
        self.mark = mark
        self.model = model
        self.number = number

    def getInfo(self):
        print(self.mark, " - ",  self.model, " - ", self.number)
        
