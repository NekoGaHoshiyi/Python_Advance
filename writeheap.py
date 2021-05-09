
# 大顶堆构建，升序排列
# 维护堆
# L为list，i为一个索引值


# 利用堆维护，寻找最大元素的索引
def heapify(L, length ,i):
    largest = i
    lchild = 2*i+1
    rchild = 2*i+2
    # 判断左孩子会不会更大
    if lchild < length and L[lchild] > L[largest]:
        #L[largest], L[lchild] = L[lchild], L[largest]
        largest, lchild = lchild, largest
    if rchild < length and L[rchild] > L[largest]:
        #L[largest], L[rchild] = L[rchild], L[largest]
        largest, rchild = rchild, largest
    if largest != i:
        L[largest], L[i] = L[i], L[largest]
        # 递归是因为自下而上，上去后，可能交换完还会出现下面比交换后还大的情况
        heapify(L, length , largest)

def heapsort(L):
    length = len(L)

    # 先建堆
    i = (length-1)//2
    while i >= 0:
        heapify(L, length, i)
        i-=1
    # 让L[0]和非完全有序的最后元素不断交换，并重新获得最大值到L[0]
    while length > 0:
        L[0], L[length-1] = L[length-1], L[0]
        length-=1
        # 因为堆已经建立，只需对0下标推举最大元素
        heapify(L, length, 0)
    return L

l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
print(heapsort(l))

