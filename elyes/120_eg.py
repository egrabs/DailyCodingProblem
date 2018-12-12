# Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances.
# And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the second instance.

class singletonWithATwist:
    def __init__(self, constructor, *args):
        self.callCount = 0
        self.firstInstance = None
        self.secondInstance = None
        self.constructor = constructor
        self.args = args

    def getInstance(self):
        if self.callCount % 2 == 0:
            if self.firstInstance is None:
                self.firstInstance = self.constructor(*self.args)
            return self.firstInstance
        elif self.callCount % 2 == 1:
            if self.secondInstance is None:
                self.secondInstance = self.constructor(*self.args)
            return self.secondInstance
        self.callCount += 1
