class Potatoes():
    def __init__(self, type, weight, time)
        self.type = type
        self.weight = weight
        self.time = time

    def time_left_mature(self):
        time_left = 10 - self.time
        print("There are {} months left till the {} is mature".format(time_left, self.type + "potato"))
    
    def grow_heavy(self)
        new_weight = (10 - self.time) * 3 + self.weight
        print("The potato will become {} pounds".format(new_weight))

    def change_type(self, type)
        self.type = type
        print("Potato type has now been set to {}".format(self.type))

    
