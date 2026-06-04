nums = [2,5,9,14,18]
target = 19


for i in range(0,len(nums)):

     num1 = nums[i]

     for j in range(i+1,len(nums)):

         num2 = nums[j]
         if num1 + num2  == target:
            print("Output is:",i,j)
            
         