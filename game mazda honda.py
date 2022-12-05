import time


class Car():
    "eto sorevnovanie mejdu hondoi i mazdoi"
    def __init__(self, model,weight,speed,category):
        self.speed = speed
        self.weight = weight
        self.model = model
        self.category = category


class Detail_info(Car):
    def __init__(self,model,weight,speed,category,color,door):
        super().__init__(model,weight,speed,category)
        self.color = color
        self.door = door

class Made_in(Car):
    def __init__(self,model,weight,speed,category,country):
        super(Made_in, self).__init__(model,weight,speed,category)
        self.country = country

    def check(self):
        print(f"This car made in {self.country}")

    def drive(self):
        print("This car is",self.model, self.weight, self.speed, self.category,self.color,self.door)


honda = Detail_info('Honda',2000,150,'sedan','black',4)
mazda = Made_in("Mazda",1500,120,"sedan","Germany")
# honda.drive()
mazda.check()

def racing(distance):
    new_distance = distance

    while distance > 0 and new_distance > 0:
        time.sleep(1)
        print(f"this distance is for {distance}")
        print(f"this distance is for {new_distance}")
        distance -= honda.speed
        new_distance -= mazda.speed
    if distance > new_distance:
        print(f"winner is {mazda.model}")
    elif distance < new_distance:
        print(f"winner is {honda.model}")
    else:
        print("Friendship")
racing(2000)

