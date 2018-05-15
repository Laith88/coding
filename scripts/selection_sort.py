
class Sort(object):
    def selection_sort(list_in):
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