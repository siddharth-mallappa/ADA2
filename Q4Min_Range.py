def minRange(lll):
    import heapq
    heap = []
    num_elts = 0
    for k in range(0,len(lll)):
        li = lll[k]
        if len(li)==0:
            print ('none of the lists can be empty')
            return 0
        num_elts += len(li)
        heapq.heappush(heap,(li[0],k))
        oldrangemin = min(heap)[0]
        oldrangemax = max(heap)[0]
        oldheaprange = oldrangemax - oldrangemin
    for i in range(0,num_elts):
            heap_min_elt = heapq.heappop(heap)
            k = heap_min_elt[1]
            heap_new_elt = lll[k].pop(0)
            heapq.heappush(heap, (heap_new_elt,k))
            rangemin = min(heap)[0]
            rangemax = max(heap)[0]
            newheaprange = rangemax - rangemin
            if newheaprange < oldheaprange:
                oldheaprange = newheaprange
                oldrangemin = rangemin
                oldrangemax = rangemax
            if len(lll[k])==0:
                break
    return [oldrangemin, oldrangemax]
