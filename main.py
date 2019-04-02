from find_diff_ids import FindDiffIds

list_of_ids = []
with open('Input Data.txt') as fin:
    for line in fin:
        list_of_ids.append(line.strip())

find = FindDiffIds()
#Find difference by 1 char
result = find.find_diff(list_of_ids, 1)
print(result)

