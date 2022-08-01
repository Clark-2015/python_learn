# try ... except xxxError ... else ...
#       to get exceptions to avoid application hash.

while True:
    a=input("a:")
    if a=="q":
        break
    b=input("b:")
    if b=="q":
        break

    # when b is zero, there will be a ZeroDivisionError to hash application
    #   use try-except-else to catch this error
    try:
        c=int(a)/int(b)
    except ZeroDivisionError:
        print("b can not be zero!")
    except ValueError:
        print("a or b must be a intenger.")
    else:
        print("a/b: "+str(c))
