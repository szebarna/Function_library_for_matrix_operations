from matrix_fuggvenykonyvtar import myfunctions
def main():
    matr =[
        [1,4,8],
        [2,4,5]
        ]
    
    matr2 =[
        [1,2],
        [3,4]
        ]
    
    """matr =[
        [1,2,3],
        [2,3,4]
        ]

    matr2 =[
        [2,2,3],
        [2,2,3],
        [2,2,3],
        [2,2,3]
        ]"""

    
    matrix2 = myfunctions.Matrix(matr)
    matrix = myfunctions.Matrix(matr2)
    print(myfunctions.matrix_inverze(matrix))
main()