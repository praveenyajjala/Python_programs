def largenumber(nums):
    if len(nums)==1:
        return str(nums[0])
    for i in range(len(nums)):
        nums[i]=str(nums[i])
    for i in range(len(nums)):
        for j in range(1+i,len(nums)):
            if nums[j]+nums[i]>nums[i]+nums[j]:
                nums[i],nums[j]=nums[j],nums[i]

    result=''.join(nums)
    if(result=='0'*len(result)):
        return '0'
    else:
        return str(result)
if __name__ =="__main__":
    nums=list(map(int,input().split()))
    print(largenumber(nums))
##    print(type(largenumber(nums)))
    .3
