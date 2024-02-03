# Jordan Bennett ##
# Fundamentals of Programming - Week 4 Collections Homework ##

# input('Starting off with Question 1') # Checked and completed.
mytuple1 = ("Car", [24, 23, 8], False, [15, 20, 11])
mytuple1_list = list(mytuple1)
access_value = mytuple1_list[3][1]
print(access_value)


# input('Continuing to Question #2') # Completed and checked.
# input('Slice the last 3 elements of the given list: List1 = [44, 12, 578, 21, 134, 67].')
List1 = [44, 12, 578, 21, 134, 67]
print(List1[3:])

# input('Question #3..') # Completed and checked.
# input('Write a program to replace 20 with 200 in list1 = [5, 10, 15, 20, 75, 100, 50]')
list1 = [5, 10, 15, 20, 75, 100, 50]
# input('Using list index to get the position of 20')
# print(list1.index(20))
list1[3] = 200
print(list1)


# input('Question #4..') # Completed and checked.
# input('Change the value of 33 to 66 in the given Tuple1 = (11, [64, 33], 243, 123)')
Tuple1 = (11, [64, 33], 243, 123)
Tuple1[1][1] = 66
print(Tuple1)

# input('Question #5..') # Completed and checked.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
uniqueset = set1.union(set2)
print(uniqueset)

# input('Question 6..') # Completed and checked.

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
modlist = list1[1::2] + list2[0::2]
print(str(modlist))

# input('Question 7 :) ..') # Completed and checked.

listr1 = [34, 54, 67, 89, 11, 43, 94]
item4 = listr1[4]
listr1.remove(item4)
listr1.insert(2, item4)
listr1.insert(8, item4)
print(listr1)


# input('Question 8..') # Completed and checked.
list21 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list22 = [7000]

list21[2][2].extend(list22)
print(list21)

# input('Question 9.. ') # Completed and checked.

primlist = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
secolist = ["h", "i", "j"]
primlist[2][1][2].extend(secolist)

print(primlist)


# input('Question 10:') # Checked and completed.
orgtuple = (40, 19, 234, 12, 10, 123)
modtuple = reversed(orgtuple)
print(tuple(modtuple))

# input("Question 11:") # Completed and checked.

dict1 = {
    "course": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(dict1['course']['student']['marks']['history'])
