a = int(input("Choose any number between 1-10 : "))

match a:
    case 1:
        print("you won 10rs voucher")
    case 5:
        print("you won 15rs voucher")
    case 7:
        print("you won 100rs voucher")
    case _:
        print("Laura pakad 🤣🤣")