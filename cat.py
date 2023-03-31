import animal

class Cat(animal.Animal):
    def __init__(self,hair,name, color, age, sex):
        self.hair = hair
        super().__init__(name, color, age, sex)


    def catch(self):
        print('i can catch mouse')

    def shout(self):
        print('miaomiao')

if __name__=='__main__':
    keke = Cat('long','keke','black','5','femail')
    keke.catch()
    keke.shout()
    keke.run()