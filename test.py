number_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

count = 0
for i in range(len(number_list)):
    for j in range(len(number_list)):
            if ((number_list[i] + number_list[j]) % 6 == 0):
                if (i != j):
                    print(number_list[i], number_list[j])
                    count += 1

print(count)