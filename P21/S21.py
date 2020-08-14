import re

P = input()
''' (?=) Is assertion lookhead
    it asserts that in the string there will be 6 characters({6}) and all of them will be intergers(\d) and string will then end there($)'''
regex_integer_in_range = r"(?=\d{6}$)"	# Do not delete 'r'.

'''It asserts that there will be a group of one digit((\d)) and then there will be another digit and then third digit will be the same as digit in first group (\1)'''
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"	# Do not delete 'r'.
print (bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
