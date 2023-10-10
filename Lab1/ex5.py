

matrix = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]

def SpiralMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    top = 0
    bottom= rows - 1
    left= 0
    right= cols - 1
    result=[]

    while top <= bottom and left <= right:
        # draepta
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # in jos
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # stanga
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # in sus
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
                left += 1
        return result


print("Matrix readed in spiral is:" , str(SpiralMatrix(matrix)))
