class box():
    def __init__(self) -> None:
        self.h = 0
        self.w = 0

    def __init__(self, height, width):
        self.h = height
        self.w = width

    def printVal(self):
        print("height: ", self.h)
        print("width: ", self.w)
        

class boxWeight(box):
    def __init__(self, height, width, weight):
        super().__init__(height, width)
        self.weight = weight

    def printVal(self):
        print("height: ", self.h)
        print("width: ", self.w)
        print("weight: ", self.weight)

    def printValP(self):
        super().printVal()



# box1 = box(4,5)
# print(box1.h)

# boxWeight1 = boxWeight(2,3,4)
# boxWeight1.printValP()
        
box1 = boxWeight