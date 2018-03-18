''' function bisect that takes a sorted list and target value
and returns the index of the value in the list if it's there, or None if it is not.
'''

def bisect(sorted_list, target):
    if len(sorted_list) < 1:
        return None
    return bisearch(sorted_list, 0, len(sorted_list)-1, target)

def bisearch(sorted_list, start, end, target):
    # print(sorted_list, 'start=', start, 'end=', end, 'target=', target)
    if (start > end):
        return None
 
    mid = (start + end) // 2
    if (sorted_list[mid] == target):
        return mid
    elif (sorted_list[mid] > target):
        return bisearch(sorted_list, start, mid - 1, target) 
    else:
        return bisearch(sorted_list, mid + 1, end, target)

def test(list, target):
    print('finding %s in the sorted list %s: %s' % (target, list, bisect(list, target)))

sorted_list = [ 'a', 'b', 'c', 'd', 'e']

test(sorted_list, 'b')
test(sorted_list, 'f')
test([], 'b')

