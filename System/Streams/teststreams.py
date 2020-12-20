"read numbers till eof and show squares"

def interact():
    print('Hello stream world') # print send to sys.stdout
    while True:
        try:
            reply = input('Enter a number>')
        except EOFError:
            break # raises an exception on eof
        else:
            # input given as a string
            num = int(reply)
            print(f"{num} squared is {num**2}")
    print('bye')

if __name__ == '__main__':
    interact() # when run, not imported
    