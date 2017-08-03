import re

fh = open('regex_sum_11334.txt')

total = 0

for line in fh:
    nums = re.findall('[0-9]+', line)
    for num in nums:
        total = total + int(num)

print(total)


print( sum([ int(num) for num in re.findall('[0-9]+', open('regex_sum_11334.txt').read())]) )
