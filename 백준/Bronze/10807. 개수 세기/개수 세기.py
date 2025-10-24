int_num = int(input())
list_num = []

list_num = list(map(int, input().split(" ", int_num)))

find_num = int(input())

print(list_num.count(find_num))
