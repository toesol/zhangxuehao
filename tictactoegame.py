
list_a = []
for i in range(10):
    list_a.append(str(i))

print(list_a)
print("Tic Tac Toe Game")
print("|____|____|____|")
print("| %s  | %s  | %s  |" % (list_a[7], list_a[8], list_a[9]))
print("|____|____|____|")
print("| %s  | %s  | %s  |" % (list_a[4], list_a[5], list_a[6]))
print("|____|____|____|")
print("| %s  | %s  | %s  |" % (list_a[1], list_a[2], list_a[3]))
print("|____|____|____|")


list_a = []
for i in range(10):
    list_a.append(" ")

def is_win(list_a):
    if (list_a[1] == list_a[2] == list_a[3] !=" ") or (list_a[4] == list_a[5] == list_a[6] !=" ") or (list_a[7] == list_a[8] == list_a[9] !=" ") or (
            list_a[1] == list_a[4] == list_a[7] !=" ") or (list_a[2] == list_a[5] == list_a[8] !=" ") or (list_a[3] == list_a[6] == list_a[9] !=" ") or (
            list_a[1] == list_a[5] == list_a[9] !=" ") or (list_a[3] == list_a[5] == list_a[7] !=" "):
        return True
    return False

count = 0
while True:
    count += 1
    number = int(input("Enter the location you want"))
    flag = "X" if count % 2 == 1 else "O"
    list_a[number] = flag

    print("|____|____|____|")
    print("| %s  | %s  | %s  |" % (list_a[7], list_a[8], list_a[9]))
    print("|____|____|____|")
    print("| %s  | %s  | %s  |" % (list_a[4], list_a[5], list_a[6]))
    print("|____|____|____|")
    print("| %s  | %s  | %s  |" % (list_a[1], list_a[2], list_a[3]))
    print("|____|____|____|")
    if is_win(list_a):
     print("Game over")
     break
