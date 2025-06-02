import time

a =  input("what would u like to do (sum,product,divide,subtract): ")
if a == "sum":
    time.sleep(1)
    print("ok")
    b = int(input("give the number: "))
    time.sleep(0.6)
    c = int(input("give another no.: "))
    time.sleep(0.6)

    result = b+c
    print(result)

elif a == "product":
    time.sleep(0.6)
    print("Thats work perfectly!")
    time.sleep(0.6)
    d = int(input("Give me then number: "))
    time.sleep(0.6)
    e = int(input("Give another number: "))
    time.sleep(0.5)

    result2 = d*e
    print(result2)

elif a == "divide":
    time.sleep(0.6)
    a1 = int(input("Ok give the number: "))
    time.sleep(0.6)
    a2 = int(input("give another number: "))
    time.sleep(0.5)

    result3 = a1/a2
    print(result3)

elif a == "subtract":
    time.sleep(0.7)
    print("Oh! that a nice choice")
    a3 = int(input("Give me the number please: "))
    time.sleep(0.7)
    a4 = int(input("Kindly provide me another number: "))
    time.sleep(0.5)

    result4 = a3-a4
    print(result4)

else:
    time.sleep(0.6)
    print("OH! looks like u have written some wrong")
