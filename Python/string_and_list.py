"""
In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day".
Then create a new string where the word "day" is replaced with the word "month".
"""

# wishes = "It's thanksgiving day. It's my birthday,too!"
# print(wishes.find("day"))
#
# for wish in wishes.split():
#     if wish == "day.":
#         wishes = wishes.replace(wish, "Month")
#         print(wishes)


"""
Min and Max
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
"""


# def find_value (a_list):
#         print(max(a_list))
#         print(min(a_list))
#
#
# find_value([2,54,-2,7,12,98])


"""
First and Last
Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. 
Now create a new list containing only the first and last values in the original list. Your code should work for any list.
"""
x = ["hello",2,54,-2,7,12,98,"world"]
length = len(x)
print(x[0])
print(x[length-1])
