#You will be given a list. You have to print a list whose 1st element should be largest and 2nd should be
# the smallest then the 3rd should be 2nd largest and 4th should be 2nd smallest and so on.


def find_list(list1):
    length=len(list1)
    sorted(list1, reverse=True)
    print("The largest number is", list1[length-1])
    print("The smallest number is",list1[0])
    print("The second largest number is", list1[length-2])
    print("The second smallest number is", list1[1])


list1=[1,2,3,4,5,6]
largest=find_list(list1)
