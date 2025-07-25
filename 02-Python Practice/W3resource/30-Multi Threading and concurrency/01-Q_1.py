import threading
def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left,right)


def merge(left,right):
    merged = []
    l = 0
    r = 0 

    while len(left) > l and len(right) > r:
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    while len(left) > l:
        merged.append(left[l])
        l += 1
    
    while len(right) > r:
        merged.append(right[r])
        r += 1

    return merged


lidt = [7,4,6,3,2,9,1,8]

#print(merge_sort(lidt))


def merge_thread(arr,thread):
    size = len(arr) // thread
    sublists = [ arr[i:i+size]  for i in range(0,len(arr),size)]
    print(sublists)
    
    threads = []
    sorted_sublists = []
    for sublist in sublists:
        thread = threading.Thread(target= lambda sublist : sorted_sublists.append(merge_sort(sublist)) , args=(sublist,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    merged = sorted_sublists[0]
    for i in range(1,len(sorted_sublists)):
        merged=merge(sorted_sublists[i],merged)
    return merged


print(merge_thread(lidt,2))