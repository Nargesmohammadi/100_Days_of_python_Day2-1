print("hello"[0])
print(len("hello"))
print("hello" + "world")
print("123" + "456")
print(123+456)
print(123_456_789)
print(123456)
num_char = len(input("what is your name?"))
new_num_char = str(num_char)
print("your name has" + new_num_char + "characters")
print(70 + float("100.5"))
print(str(70) + str(100))
three_digit_number = input("enter three number\n")
print(str(three_digit_number))
first_digit_number = three_digit_number[0]
second_digit_number = three_digit_number[1]
third_digit_number = three_digit_number[2]
result = first_digit_number + second_digit_number + third_digit_number
print(result)
result = int(third_digit_number) + int(first_digit_number) + int(second_digit_number)
print(result)
three_digit_number = second_digit_number + first_digit_number + third_digit_number
print(three_digit_number)
