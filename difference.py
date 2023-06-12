file1 = open("C:/Users/gautams/Downloads/Synchronisation during code promotion/abc.txt", "r")
file2 = open("C:/Users/gautams/Downloads/Synchronisation during code promotion/def.txt", "r")

i = 0

for l1 in file1:
    i += 1
    for l2 in file2:
        if l1 == l2:
            print("Line ", i,": ")
            print("Both the lines are same")
        else:
            print("Line ", i,": ")
            print("File 1: ", l1)
            print("File 2: ", l2)
        break

file1.close()
file2.close()