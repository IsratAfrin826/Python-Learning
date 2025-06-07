#parent class, super class , base class
#child class, sub class, derived class

class phone:
    def call(self):
        print("you can call")
    def message(self):
        print("you can message")


class samsung(phone):
    def photo(self):
        print("you can take photo")



s = samsung()
s.call()
s.message()
s.photo()
print(issubclass(samsung,phone))
