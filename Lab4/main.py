# -----------------------------------------Exercitiul 1

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Example usage of the Stack class
# stack = Stack()
#
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# print("Stack peek:", stack.peek())  # Output: 3
# print("Stack size:", stack.size())  # Output: 3
#
# print("Popped item:", stack.pop())  # Output: 3
#
# print("Stack peek after pop:", stack.peek())  # Output: 2
# print("Is stack empty?", stack.is_empty())  # Output: False


# -----------------------------------------Exercitiul 2

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Example usage of the Queue class
# queue = Queue()
#
# queue.push(1)
# queue.push(2)
# queue.push(3)
#
# print("Queue peek:", queue.peek())  # Output: 1
# print("Queue size:", queue.size())  # Output: 3
#
# print("Popped item:", queue.pop())  # Output: 1
#
# print("Queue peek after pop:", queue.peek())  # Output: 2
# print("Is queue empty?", queue.is_empty())  # Output: False


# -----------------------------------------Exercitiul 3


class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.matrix = [[0 for _ in range(m)] for _ in range(n)]

    def get(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.matrix[i][j]
        else:
            return None

    def set(self, i, j, value):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.matrix[i][j] = value

    def transpose(self):
        transposed_matrix = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                transposed_matrix[j][i] = self.matrix[i][j]
        self.matrix = transposed_matrix
        self.rows, self.cols = self.cols, self.rows

    def multiply(self, other):
        if self.cols != other.rows:
            return None

        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result

    def apply_function(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = func(self.matrix[i][j])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])


# Example usage of the Matrix class
matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)

print("Original Matrix:")
print(matrix)

print("Element at (1, 2):", matrix.get(1, 2))  # Output: 6

matrix.transpose()
print("Transposed Matrix:")
print(matrix)

# Example of applying a transformation function (squaring all elements)
matrix.apply_function(lambda x: x ** 2)
print("Matrix after applying transformation function:")
print(matrix)

# Example of matrix multiplication
matrix2 = Matrix(2, 3)
matrix2.set(0, 0, 1)
matrix2.set(0, 1, 2)
matrix2.set(0, 2, 3)
matrix2.set(1, 0, 4)
matrix2.set(1, 1, 5)
matrix2.set(1, 2, 6)

result = matrix.multiply(matrix2)
if result:
    print("Result of matrix multiplication:")
    print(result)
else:
    print("Matrices cannot be multiplied due to incompatible dimensions.")
