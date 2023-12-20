class Car:
    
    def __init__(self, brand,mileage, color,is_autometic,):
        self.brand= brand
        self.mileage = mileage
        self.color =color
        self.is_autometic = is_autometic
    

    def show_features(self):
    
        print(self.brand)
        print(self.mileage)
        print(self.color)
        print(self.is_autometic)
        if self.is_autometic==True:
            print("Automatic")
        elif self.is_autometic==False:
            print("Manual")
        else:
            print("Give a valid input")
       
car1 = Car("Volkswagen",20,"Blue",True)
car2=Car("Honda",25,"Red",False)

car1.show_features()
car2.show_features()



