class Car:

    # create class attributes
    car_count = 0
    '''
    def __init__(self,name, make, model):
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1
    '''
    # create class methods
    def start(self, name, make, model):
        print ("Engine started "+name)
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1
    


def main():
    car_a = Car()
    car_a.start("Ignis", "Maruti", 2015)
    print(car_a.name)
    print("Workshop")

if __name__ == "__main__":
    main()




