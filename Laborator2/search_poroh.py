# search

c = int(0)
def search(haystack, needle):
    global c
    c = 0
    for i in haystack:
        print("- ", i)
        print("= ", needle)
        print("=== ", int(i) == int(needle))
        if (int(i) == int(needle)):
            print("FOUND ELEMENT")
            return c
        c += 1
    return False

# binary search
# def binarySearch(haystack, needle):


# input data
number_list = []
neendle = int(input("element to find: "))
print("\n")
n = int(input("Insert # of elements: "))
print("\n")
for i in range(0, n):
    print("Insert element for: ", i, " ")
    item = int(input())
    number_list.append(item)
print("The list is", number_list)


# output data
find = search(number_list, neendle)
if find != False:
    print("we found element on pos: ", find)
else:
    print("we didn't find the element: ", neendle)