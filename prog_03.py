nums = [2,5,11,18,20,15,19,12]

##def compare(nums):
state = False
print(len(nums))
print(nums[8])
for i in range(0,len(nums)-1): 
                 
    num1 = nums[i]

    for j in range(i+1,len(nums)): 
        num2=nums[j]
        if num1 == num2:
            print("True")
            state = True
            break
    print(state)                                 
##               print(output)
    if state:
    
        break
    ##break

