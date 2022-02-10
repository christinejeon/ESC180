def display_current_value():
    print("Current value:", current_value)

saved_value = 0
def save():
    global saved_value
    global current_value
    saved_value = current_value

saved_for_undo = 0
def save_for_undo():
    global saved_for_undo
    global current_value
    saved_for_undo = current_value

def add(to_add):
    save_for_undo()
    global current_value
    current_value += to_add

def mult(to_mult):
    save_for_undo()
    global current_value
    current_value *= to_mult

def divide(to_divide):
    save_for_undo()
    global current_value
    if to_divide == 0:
        print("Cannot divide by zero.")
        return
    else:
        current_value /= to_divide

def recall():
    global saved_value
    global current_value
    current_value = saved_value

def undo():
    global saved_for_undo
    global current_value
    temp = saved_for_undo
    save_for_undo()
    current_value = temp


if __name__ == "__main__":
    current_value = 0

    print("Welcome to the calculator program.")
    print("Current value: " + str(current_value))
'''
    display_current_value()
    add(5)
    display_current_value()
    mult(3)
    display_current_value()
    divide(2)
    display_current_value()
    divide(0)
    display_current_value()
    save()
    mult(2)
    display_current_value()
    recall()
    display_current_value()
'''

    display_current_value() # 0
    add(5) # 5
    display_current_value() # 5
    undo()
    display_current_value() # 0
    undo()
    display_current_value() # 5
    mult(10)
    display_current_value() # 50
    undo()
    undo()
    display_current_value() # 50
    undo()
    undo()
    undo()
    display_current_value() # 5
