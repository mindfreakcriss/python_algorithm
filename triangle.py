# coding=utf-8
import csv
import sys

#length = int(sys.argv[1])


def triangle(n):
    for i in range(n):
        index = i + 1
        len = 2 * index - 1
        print(("*" * len).center(2 * n - 1))


#triangle(length)


def factional(n):
    if n == 1:
        return 1
    else:
        return factional(n-1) + 1 / n


#print(factional(length))

# 文本文件
def file_operation(file):
    lines = open(file, 'r')
    try:
        for s in lines:
            print(s, end="")
    finally:
        lines.close()


#file = "/Users/huangkaibo/Desktop/dd.txt"
#file_operation(file)

# 二进制文件

# def binary_operation(file):
#     content = open(file, 'wb')
#     content.write("") #写入文件
#     content.flush() #缓冲写入
#     content.close()


# csv 文件

def readcsv(csvfilepath):
    with open(csvfilepath, newline= "") as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        print(headers)
        for row in  f_csv:
            print(row)

# JSON 对象

def json_dump():
    return 
    # dumps(obj) obj 对象序列化为JSON字符串
    # dump(obj, fp) obj 对象序列化为JSON字符串写入文件fp
    # loads(s) JSON字符串s 反序列化后的对象
    # load(fp) 返回从文件 fp 中读取的JSON 字符串反序列化后的对象