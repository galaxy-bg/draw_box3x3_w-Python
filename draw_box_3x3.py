class box():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print("X değeri: {}\nY değeri: {}\n".format(self.x,self.y))

    def draw(self):
        for row in range(self.x):
            for col in range(self.y):
                if (row==0 and col==0) or (row==0 and col==self.y-1) or (row==self.x-1 and col==0) or (row==self.x-1 and col==self.y-1):
                    print("+",end=" ")
                elif ((row==0 or row==self.x-1) and (col!=0 or col!=self.y-1)):
                    print("-",end=" ")
                elif ((col==0 or col==self.y-1) and (row!=0 or row!=self.x-1)):
                    print("|",end=" ")
                else:
                    print(" ",end=" ")
            print()

# Create 3x3 Box and Draw             
box3x3 = box(3,3)
box3x3.draw()
