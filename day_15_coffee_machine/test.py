a=10
def func():
    global a
    a+=10
    print("Value inside the function:",a)
func()
print("Value Outside the function:",a)