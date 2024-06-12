# Q. Given a list sort the element in the decreasing order of occurences.
 
# Input: nums = [1,2,6,6,8,6,9,5,6,3,4,2,5,6,3,8,7,6,9,4,2,1,2,1,2,4,5]
# Output: [6, 6, 6, 6, 6, 6, 2, 2, 2, 2, 2, 1, 1, 1, 5, 5, 5, 4, 4, 4, 8, 8, 9, 9, 3, 3, 7]
 
# Input: nums = [5,5,2,3,2,2,3,4,5,2,1,3,2,1,6,6,3,2,1,4,5,5]
# Output: [2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 1, 1, 1, 4, 4, 6, 6]

def sort_occ(num):
    num_occ = {}
    for i in num:
        if i in num_occ:
            # num_occ[i]+=1
            num_occ[i] = num_occ[i] + 1
        else:
            num_occ[i] = 1
    
    # sort_g = [x for x,count in num_occ.items() if]
    result = sorted(num_occ.items(), key=lambda x:x[1], reverse=True)
    res = []
    for item, count in result:
        res.extend([item] * count)
    
    return res

input_list = [1,2,6,6,8,6,9,5,6,3,4,2,5,6,3,8,7,6,9,4,2,1,2,1,2,4,5]

y = sort_occ(input_list)

print(y)