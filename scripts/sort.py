
class InsertionSort(object):
    def sort(self, list_in):
        if list_in is None:
            return TypeError('input can not be None')
        if len(list_in)<2:
            return list_in
        for inseration_index in range(1, len(list_in)):
            for next_index in range(inseration_index):
                if list_in[inseration_index] < list_in[next_index]:
                    tmp = list_in[inseration_index]
                    list_in[next_index+1:inseration_index+1] = list_in[next_index:inseration_index]
                    list_in[next_index] = tmp
        return list_in
    
class SelectionSort(object):
    def sort(self, list_in):
        if list_in is None:
            raise TypeError('input can not be None')
        if len(list_in) < 2:
            return list_in
        for selected_index in range(len(list_in)-1):
            temp = selected_index
            for next_index in range(selected_index+1, len(list_in)):
                if list_in[next_index] < list_in[temp]:
                    temp = next_index
            list_in[temp], list_in[selected_index] = list_in[selected_index], list_in[temp]
        return list_in
    
class MergeSort(object):
    """ Sort a list based on the merge sort algorithm """
    
    def sort(self, list_in):
        if list_in is None:
            raise TypeError('input list can not be none')
        return self._sort(list_in)
    
    def _sort(self, list_in):
        if len(list_in)<2:
            return list_in
        mid = len(list_in)//2
        right = list_in[:mid]
        left = list_in[mid:]
        right_ = self._sort(right)
        left_ = self._sort(left)
        return self._merge(left, right)
    
    def _merge(self, left, right):
        index_l = 0
        index_r = 0
        result = []
        while index_l < len(left) and index_r < len(right):
            if left[index_l] < right[index_r]:
                result.append(left[index_l])
                index_l += 1
            else:
                result.append(right[index_r])
                index_r += 1
        while index_l < len(left):
            result.append(left[index_l])
            index_l += 1
        while index_r < len(right):
            result.append(right[index_r])
            index_r += 1
        return result

class QuickSort(object):
    def quick_sort(self, list_in):
        if list_in is None:
            raise TypeError('input can not be None')
        return self._quick_sort(list_in)

    def _quick_sort(self, list_in):
        if len(list_in) < 2:
            return list_in
        left = []
        right = []
        equal = []
        pivot = list_in[len(list_in)//2]
        for element in list_in:
            if element == pivot:
                equal.append(element)
            elif element > pivot:
                right.append(element)
            else:
                left.append(element)

        if len(left)>len(right):
            _left = self._quick_sort(left)
            _right = self._quick_sort(right)
        else:
            _right = self._quick_sort(right)
            _left = self._quick_sort(left)
        return _left + equal + _right