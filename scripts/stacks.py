class Stacks(object):
    
    def __init__(self, stack_size, stack_num):
        self.stack_size = stack_size
        self.stack_num = stack_num
        self.stack_pointer = [-1] * stack_num
        self.stack_array = [None] * stack_num * stack_size
    
    def abs_index(self, stack_index):
        return stack_index * self.stack_size + self.stack_pointer[stack_index]
    
    def push(self, data, stack_index):
        if self.stack_pointer[stack_index] == self.stack_size -1:
            raise Exception('Stack is full')
        self.stack_pointer[stack_index] += 1
        array_pointer = self.abs_index(stack_index)
        self.stack_array[array_pointer] = data
        
    def pop(self, stack_index):
        if self.stack_pointer[stack_index] == -1:
            raise Exeption('Stack is empty')
        array_pointer = self.abs_index(stack_index)
        data = self.stack_array[array_pointer]
        self.stack_array[array_pointer] = None
        stack_pointer[stack_index] -= 1
        return data