class Hello:

    def __init__(self, name):
        self.name=name
        print("step1" + name)

    def say_hello(self ):
        print("Hello " + self.name)

h = Hello('Ramweet')
h.say_hello()
