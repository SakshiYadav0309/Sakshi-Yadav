# classname =0

# while classname <=7:
#     print("class:",classname)
#     for i in range(1,11):
#         print(i,end="")
#     print("\n attendence done")
#     classname +=1


# rollnumber = 0
# branchname = ["cse","ece","mech","civil","eee"]

# for branch in branchname:
#     print("branch:",branch)
#     for rollnumber in range(1,11):
#         print(rollnumber, end=" ")
       
#     print("\n attendence done\n")
#     rollnumber += 1    

import time

for round in range(1,4):
    print("round:",round)
    count = 3
    while count >0:
        print("countdown:",count)
        time.sleep(2)
        count -= 1
    print("round finished")
    print("next round")












