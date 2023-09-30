def find_closest_to_zero(nums):
    nums.sort()  
    n = len(nums)
    min_sum = float('inf')
    min_diff = float('inf')
    closest_nums = None
    
   
    left = 0
    right = n - 1
    
    while left < right:
        curr_sum = nums[left] + nums[right]
        curr_diff = (abs(nums[left]) - abs(nums[right]))
        
        
        if curr_sum < min_sum:
            min_sum = curr_sum
            closest_nums = (nums[left], nums[right])

        if((curr_sum == min_sum)) :
            if curr_diff < min_diff:
                min_diff = curr_diff
                closest_nums = (nums[left], nums[right])
                
                if curr_diff<0:
                    left+=1
                else:
                    right-=1


        
        if curr_sum < 0:
            left += 1
        else:
            right -= 1
        
    
    return closest_nums


nums = input("Enter the array of integers (space-separated): ").split()
nums = [int(num) for num in nums]

closest_pair = find_closest_to_zero(nums)
print("The two numbers with the sum closest to zero and smallest absolute difference are:", closest_pair)
