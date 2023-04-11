# coding=utf-8

# formula 1
# import sys, random
#
# n = int(sys.argv[1])
#
# for i in range(n):
#     print(random.randrange(0, 100))

# formula 2
# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument('--length', default=10, type=int, help='length')
#
# parser.add_argument('--width', default=5, type=int, help='width')
#
# args = parser.parse_args()
#
# area = args.length * args.width
#
# print("the area is", area)

# formula 3
# import datetime
#
# sName = input("请输入您的姓名:")
# birthyear = int(input("请输入你的出生年份："))
# age = datetime.date.today().year - birthyear
# print("您好！{0}, 你{1}岁".format(sName, age))

import sys

total = 0.0
count = 0
for line in sys.stdin:
    count += 1
    total += float(line)
avg = total / count
print("avg is {0}", avg)