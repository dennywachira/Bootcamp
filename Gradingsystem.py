num = int(input('please enter your mark:\n'))

if num <=100 and num>=80:
    print('you got A')
elif num<79 and num>75:
    print("you got A-")
elif num<74 and num>70:
    print("you got B+")
elif num<69 and num>65: 
     print ("you got B")
elif num<64 and num>60:
    print ("you got C+")
elif num<59 and num>55:
    print("you got C")
elif num<54 and num>50:
    print("you got a C-")
else:
    print("YOU FAILED!!")


