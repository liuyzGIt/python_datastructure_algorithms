class SortExample:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        pass

    def less(self, i, j):
        return self.arr[i] < self.arr[j]

    def exchange(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def is_sorted(self):
        for i in range(1, len(self.arr)):
            if self.less(i, i-1):
                return False
        return True
    
    def show(self):
        print(self.arr)
        print("is sorted:" + str(self.is_sorted()))

        
class BubbleSort(SortExample):
    def sort(self):
        n = len(self.arr)
        for i in range(n):
            is_sorted = True
            for j in range(n-i-1):
                if self.less(j+1, j):
                    self.exchange(j+1, j)
                    is_sorted = False
            if is_sorted:
                break

                    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        sorted = True
        # j = 0
        # while j < n-i-1 and not sorted: 
            # if arr[j+1] < arr[j]:
                # arr[j+1], arr[j] = arr[j], arr[j+1]
                # sorted = False
            # j += 1
        
        for j in range(n-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                sorted = False
        if sorted:
            print(sorted)
            break
                    

class SelectionSort(SortExample):
    def sort(self):
        n = len(self.arr)
        for i in range(n):
            mx = 0
            for j in range(n-i):
                if self.less(mx, j):
                    mx = j
            self.arr[mx], self.arr[n-i-1] = self.arr[n-i-1], self.arr[mx]
        
        
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_index = 0
        for j in range(1, n-i):
            if arr[max_index] < arr[j]:
                max_index = j
        arr[max_index], arr[n-i-1] = arr[n-i-1], arr[max_index] 


def selection_sort_2(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


class InsertionSort(SortExample):
    def sort(self):
        n = len(self.arr)
        for i in range(1, n):
            for j in range(i, 0, -1):
                if self.less(j, j-1):
                    self.exchange(j, j-1)
                    
    def sort2(self):
        n = len(self.arr)
        for i in range(1, n):
            j = i
            key = self.arr[i]
            while j > 0 and key < self.arr[j-1]:
                self.arr[j] = self.arr[j-1]
                j -= 1
            self.arr[j] = key

            
class ShellSort(SortExample):
    def sort(self):
        n = len(self.arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                j = i
                key = self.arr[j]
                while j >= gap and key < self.arr[j-gap]:
                    self.arr[j] = self.arr[j-gap]
                    j -= gap
                self.arr[j] = key
            gap = gap // 2
            
        
def quick_sort(arr, start, end):
    low = start
    high = end
    if low >= high:
        return
    
    pivot = arr[low]
    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]
        
        while low < high and arr[low] < pivot:
            low += 1
        arr[high] = arr[low]
        
    arr[low] = pivot
    quick_sort(arr, start, low-1)
    quick_sort(arr, low+1, end)   


def partition(arr,low,high): 
    povit = arr[high]
    i = (low-1)
    
    for j in range(low, high):
        if arr[j] < povit:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
    
 
# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引  
# 快速排序函数
def quick_sort2(arr,low,high): 
    if low < high:   
        pi = partition(arr,low,high)   
        quick_sort2(arr, low, pi-1) 
        quick_sort2(arr, pi+1, high) 


class QuickSort(SortExample):
    def sort(self):
        self.quick_sort(0, len(self.arr)-1)
        
    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi-1)
            self.quick_sort(pi+1, high)
    
    def partition(self, low, high):
        pivot = self.arr[low]
        i = high + 1
        for j in range(high, low, -1):
            if self.arr[j] > pivot:
                i -= 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        
        self.arr[i-1], self.arr[low] =self.arr[low], self.arr[i-1]
        return i-1


def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        c.extend(b[j:])
    else:
        c.extend(a[i:])
        
    return c

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
    
def merge2(arr, left, m, right):
    a = arr[left:m+1]
    b = arr[m+1: right+1]
    
    i = j = 0
    k = left
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1
        
def merge_sort2(arr,left, right):
    if left < right:
        m = (left + right) // 2
        
        merge_sort2(arr, left, m)
        merge_sort2(arr, m+1, right)
        merge2(arr, left, m, right)
      
        
class MergeSort(SortExample):
    def sort(self):
        arr = self.merge_sort(self.arr)
        self.arr = arr
    
    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
            
        mid = len(arr) // 2
        left = MergeSort.merge_sort(arr[:mid])
        right = MergeSort.merge_sort(arr[mid:])
        return MergeSort.merge(left, right)
    
    @staticmethod
    def merge(left, right):
        c = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                c.append(left[i])
                i += 1
            else:
                c.append(right[j])
                j += 1
        if i == len(left):
            c.extend(right[j:])
        else:
            c.extend(left[i:])
        return c


def CountingSort(a, b, k):
    #c=[0]*(k+1) #let c[0...k] be an all 0 array
    #c=[0 for i in range(0,k+1)]
    c=[]
    for i in range(k+1):
        c.append(0)
    for j in range(len(a)):
        c[a[j]] = c[a[j]] + 1
    print(c)
    for i in range(1, k+1):
        c[i] = c[i] + c[i-1]
    print(c)
    for j in range(len(a)-1, -1, -1):
        b[c[a[j]]-1] = a[j]#!!!!!减一是关键
        c[a[j]] = c[a[j]] - 1
    print(b)
    
a=[2, 5, 3, 0, 2, 3, 0, 3]

b=[None for i in range(len(a))]
CountingSort(a, b, max(a))



arr = [5,4,3,5,2,8,1,6,7]

if __name__ == "__main__":
    import timeit
    import sys
    # arr = [5,4,3,5,2,8,1,6,7,10]
    
    # print(timeit.timeit("merge_sort2(arr, 0, len(arr))", "from __main__ import arr, merge_sort2, merge2", number=100000))
    # print(timeit.timeit("merge_sort(arr)", "from __main__ import arr, merge_sort, merge", number=100000))
    # ms = MergeSort(arr)
    # print(timeit.timeit(ms.sort, number=100000))
    # ms.sort()
    # ms.show()
    
    # merge_sort2(arr, 0, len(arr))
    # print(arr)
    
    # qs = QuickSort(arr)
    # qs.sort()
    # qs.show()
    # quick_sort2(arr, 0, len(arr)-1)
    # print(arr)
    
    # shells = ShellSort(arr)
    # shells.sort()
    # shells.show()
    
    # bs = BubbleSort(arr)
    # bs.sort()
    # bs.show()
    # arr = [1,2,3,4,5]
    # bubble_sort(arr)
    # print(arr)
    
    # ss = SelectionSort(arr)
    # ss.sort()
    # ss.show()
    # selection_sort_2(arr) 
    # print(arr) 
    
    # ins = InsertionSort(arr)
    # print(timeit.timeit(ins.sort, number=100000))
    # print(timeit.timeit(ins.sort2, number=100000))
    # ins.sort2()
    # ins.show()       
    
