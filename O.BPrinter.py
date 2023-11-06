import pyperclip
# Manual ASCII art
def print_manual_ascii_art():
    art = r"""                                       
 _____        ____        ____                     __
/\  __`\     /\  _`\     /\  _`\        __        /\ \__
\ \ \/\ \    \ \ \L\ \   \ \ \L\ \_ __ /\_\    ___\ \ ,_\    __   _ __  
 \ \ \ \ \    \ \  _ <'   \ \ ,__/\`'__\/\ \ /' _ `\ \ \/  /'__`\/\`'__\
  \ \ \_\ \  __\ \ \L\ \   \ \ \/\ \ \/ \ \ \/\ \/\ \ \ \_/\  __/\ \ \/ 
   \ \_____\/\_\\ \____/    \ \_\ \ \_\  \ \_\ \_\ \_\ \__\ \____\\ \_\ 
    \/_____/\/_/ \/___/      \/_/  \/_/   \/_/\/_/\/_/\/__/\/____/ \/_/
                                                                                                                                              
    """
    print(art)
print_manual_ascii_art()


print("---------WELCOME TO O.B PRINTER---------\n")
print("To make single-sided printer to duplex printer\n".upper())

while True:
    while True:
        try:
            page = int(input("How many page you have ?:"))
            break
        except:
            print("Page is not right,please PRESS 1 to try again!!!!")
            check = int(input())
            if check == 1:
                continue
            else:
                break

    """"
    make space to insert odd and even
    """
    shiba_1 = []
    shiba_2 = []


    def get_odd(page):
        for odd in range(1, page + 1):
            if odd % 2 != 0:
                shiba_1.append(odd)


    def get_even(page):
        for even in range(1, page + 1):
            if even % 2 == 0:
                shiba_2.append(even)


    get_odd(page)
    get_even(page)

    x = ",".join(str(ele) for ele in shiba_1)
    y = ",".join(str(ele) for ele in shiba_2)
    pyperclip.copy(x)
    print("-->Your odd number is: {}".format(x))
    print("Your number has been copied\n")
    check = input("Press any key to continue\n")

    print("--->Your even number is: {}".format(y))
    print("Your number has been copied\n")
    pyperclip.copy(y)

    yes=["yes","Yes","y","Y","YES"]
    
    print("Print more? Yes to print more")
    user_choice=str(input("Your choice:  "))
    if user_choice in yes:
        continue
    else:
        print("Shiba break point")
        break

