def greet(name):
    print "Hello " + name

# Assigning functions to variables
greet_someone = greet

greet_someone("Vinesh")

# Function inside function
def new_greet(name):
    def greeting_message():
        return "Hola "

    message = greeting_message() + name
    print message

new_greet("Vinesh")

#Function passed as argument
def caller(func):
    new_name = ("ABC")

    func(new_name)

caller(greet)
caller(new_greet)

#Function returning other function
def greet_generator():
    def get_message():
        return "Hello There"

    return get_message

message_func = greet_generator()
print message_func()

def get_text(name):
    return "Hello {0}.".format(name)

def get_full_greeting(func):
    def format_greeting(name):
        return "{0}. How are you?".format(func(name))

    return format_greeting

full_greeting = get_full_greeting(get_text)
print full_greeting("Vinesh")
