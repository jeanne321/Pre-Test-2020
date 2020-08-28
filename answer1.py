# Pre-Test-2020
# Question 1

# Write a function that takes two arrays as input, each array contains a list of A-Z;
# Your program should return True if the 2nd array is a subset of 1st array, or False if not.


def outer():
    a1 = input("arr1: ").upper()
    a2 = input("arr2: ").upper()

    def isSubset(arr1, arr2):
        if all(x in arr1 for x in arr2):
            print("true")
        else:
            print("false")
    return isSubset(a1, a2)


outer()

#computational complexity: O(n ^ 2)
