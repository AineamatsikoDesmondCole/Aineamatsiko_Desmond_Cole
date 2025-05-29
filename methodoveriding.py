class Man:
    def make_sound(self):
        print("Man sound")

class Boy(Man):
    def make_sound(self):  
        print("Boy sound")

class Girl(Man):
    def make_sound(self):  
        print("Girl sound")

man = Man()
boy = Boy()
girl = Girl()

man.make_sound()  
boy.make_sound()     
girl.make_sound()