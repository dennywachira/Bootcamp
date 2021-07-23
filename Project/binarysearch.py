#Binary search Algorithm



def BinarySearch(list1,key): #define the binary Search function
    lowindex=0
    highindex= len(list1)-1
    found =False
    while lowindex<=highindex and not found:
        midelement =(lowindex+highindex)//2

        if key==list1[midelement]:               #checking if key matches our middle element
            found=True
        elif key>list1[midelement]:
            lowindex=midelement+1
        else:
            highindex=midelement-1
    if found==True:
        print("element found")
    else:
        print("Element not Found")

list1= [1,3,14,5,12,23]      #define  a list
list1.sort()                 #sort the list
print(list1)                 #printing the Sorted List

key=int(input("Enter the Key to Search\n")) #Prompt the user to enter the key to search.
BinarySearch(list1,key)   #calling the Binary Search Function