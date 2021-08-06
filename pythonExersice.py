#1.	Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
values = input("Enter the numbers:")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


#2.	Write a Python program to accept a filename from the user and print the extension of that.
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print("The extension of thr file is : " + repr(f_extns[-1]))


#3.	Write a Python program to display the first and last elements from any list.
my_list = [3,4,6,7,8]
print("The original list is : " + str(my_list))
res = my_list[::len(my_list)-1]
print("The first and last element of list are : " + str(res))


#4.	Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
def new_string(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str
print(new_string("Cody"))
print(new_string("IsEmpty"))

#5.	Write a Python program to check whether a specified value is contained in a group of values.
def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))


#6.	Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
color_list_1 = set(["Blue", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifference of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))


#7.	Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
def remove_nums(int_list):
  position = 3 - 1
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [30,40,34,48,57,63]
remove_nums(nums)

#8.	Write a Python program to count the number of characters (character frequency) in a string.
def count(str):
    d = {}
    for n in str:
        keys= d.keys()
        if n in keys:
          d[n] += 1
        else:
         d[n] = 1
    return d
print(count('keerthu.org'))
print()

#9.	Write a Python function that takes two lists and returns True if they have at least one common member
def my_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result


print(my_data([2, 4, 6, 8, 9], [5, 6, 7, 8, 9]))
print(my_data([2, 3, 4, 6, 8], [6, 7, 8, 9]))


#10.	Write a Python program that accepts a string and calculate the number of digits and letters.
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)