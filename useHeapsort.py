def big_endian(arr, start, end):
    root = start
    child = root * 2 + 1  # 左孩子
    while child <= end:
        # 孩子比最后一个节点还大，也就意味着最后一个叶子节点了，就得跳出去一次循环，已经调整完毕
        if child + 1 <= end and arr[child] < arr[child + 1]:
            # 为了始终让其跟子元素的较大值比较，如果右边大就左换右，左边大的话就默认
            child += 1
        if arr[root] < arr[child]:
            # 父节点小于子节点直接交换位置，同时坐标也得换，这样下次循环可以准确判断：是否为最底层，
            # 是不是调整完毕
            arr[root], arr[child] = arr[child], arr[root]
            root = child
            child = root * 2 + 1
        else:
            break


def heap_sort(arr):  # 无序区大根堆排序
    first = len(arr) // 2 - 1
    for start in range(first, -1, -1):
        # 从下到上，从左到右对每个节点进行调整，循环得到非叶子节点
        big_endian(arr, start, len(arr) - 1)  # 去调整所有的节点
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]  # 顶部尾部互换位置
        big_endian(arr, 0, end - 1)  # 重新调整子节点的顺序，从顶开始调整
    return arr


def main():
    l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
    print(heap_sort(l))


if __name__ == "__main__":
    main()