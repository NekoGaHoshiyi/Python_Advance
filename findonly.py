
def findone(L):
    left = 0
    right = len(L) - 1
    while left < right:
        mid = (left+right)// 2
        isone = len(L[left:mid]) % 2
        if L[mid] != L[mid-1] and L[mid] != L[mid+1]:
            return L[mid]
        if isone and L[mid] == L[mid-1]:
            left = mid + 1
        elif isone and L[mid] == L[mid + 1]:
            right = mid - 1
        elif not isone and L[mid] == L[mid-1]:
            right = mid - 2
        elif not isone and L[mid] == L[mid + 1]:
            left = mid + 2
    return L[left]
print(findone([3,3,7,7,10,11,11]))
print(findone([1,1,2,3,3,4,4,8,8]))
print(findone([9,9,1,1,2,3,3,4,4,8,8]))