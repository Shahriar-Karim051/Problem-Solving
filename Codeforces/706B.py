def next(arr, target): 
    start = 0; 
    end = len(arr) - 1; 
  
    ans = len(arr); 
    while (start <= end): 
        mid = (start + end) // 2; 
  
        # Move to right side if target is 
        # greater. 
        if (arr[mid] <= target): 
            start = mid + 1; 
  
        # Move left side. 
        else: 
            ans = mid; 
            end = mid - 1; 
  
    return ans; 
  

z = int(input())

arr = [int(a) for a in input().split()]
arr.sort()


for i in range(int(input())):
    n = int(input())
    print(next(arr , n))