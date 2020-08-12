import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

message = ''
for col in range(0,m):
    for row in range (0,n):
        message += str(matrix[row][col])


pre_message = ''
split_message = re.findall(r'^[\s#!@$%&]+',message)
decoded_message = message
for i in range(0,len(split_message)):
    pre_message = str(split_message[0])
    decoded_message = str(re.split(r'^[\s#!@$%&]+',message)[1])
     

regex_pattern = r'\w+[\s#!@$%&]+\w+'
reg = r'[\s#!@$%&]+'
start = []
end = []
pattern_string = re.match(regex_pattern,decoded_message)
while(pattern_string):
    for i in re.finditer(reg,decoded_message):
        pattern_string = i.span()
        break
    for i in range(pattern_string[0],pattern_string[1]):
        decoded_message=decoded_message[:i]+"1"+decoded_message[i+1:]
    pattern_string = re.match(regex_pattern,decoded_message)

    
decoded_message = re.sub(r'1+',' ',decoded_message)
print(pre_message+decoded_message)