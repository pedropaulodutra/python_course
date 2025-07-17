# Desafio: crie uma classe com pelo menos um atributo e um método e imprima informações dela no seu terminal

class Car:
    def __init__(self, wheels, doors, engine, is_running, gasoline):
        self.wheels = wheels
        self.doors = doors
        self.engine = engine
        self.is_running = is_running
        self.gasoline = gasoline

    def run_car(self):
        if self.is_running:
            print("car is already on")
        else:
            print("starting car")
            self.is_running = True

    def turn_off_car(self):
        if self.is_running:
            print("turning off car")
            self.is_running = False
        else:
            print("car is already off")

    def accelerate(self):
        if self.is_running and self.gasoline > 0:
            while self.gasoline > 0:
                print("car running")
                self.gasoline -= self.engine
            print("stopping car")
        elif not self.is_running:
            print("car is off")
        else:
            print("car has no gas")

bmw = Car(4, 4, 1.8, False, 200)
bmw.run_car()
bmw.accelerate()