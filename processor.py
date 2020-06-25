
def constant_x_matrix():
        n,m = [int(x) for x in input("Enter size of matrix: ").split()]
        matrix_a = []
        print("Enter matrix:")
        for i in range(n):
            i_ = [int(x) if x.isdigit() else float(x) for x in input().split()]
            matrix_a.append(i_)
        c = input("Enter constant: ")
        constant = int(c) if c.isdigit() else float(c)
        result = []
        for i in range(n):
            i_ = [0 for x in range(m)]
            result.append(i_)
        for x in range (n):
            for y in range(m):
                result[x][y] = matrix_a[x][y] * constant
        l = []
        s = ""
        print("The result is:")
        for x_ in result:
            l.append(str(x_))
            s = " ,".join(l)
        s_ = s.split(" ,")
        for y_ in s_:
            print("".join(y_).strip("[]").replace(","," "))
        print("\n")

def add_matrices():
        n,m = [int(x) for x in input("Enter size of first matrix: ").split()]
        matrix_a = []
        print("Enter first matrix:")
        for i in range(n):
            i_ = [int(x) if x.isdigit() else float(x) for x in input().split()]
            matrix_a.append(i_)
        n_,m_ = [int(x) for x in input("Enter size of second matrix: ").split()]
        matrix_b = []
        print("Enter second matrix:")
        for j in range(n_):
            j_ = [int(x) if x.isdigit() else float(x) for x in input().split()]
            matrix_b.append(j_)
        total = []
        for i in range(n):
            i_ = [0 for x in range(m)]
            total.append(i_)

        if n == n_ and m == m_:
            for i in range(n):
                for j in range(m):
                    total[i][j] = matrix_a[i][j] + matrix_b[i][j]
            l = []
            s = ""
            print("The result is:")
            for x in total:
                l.append(str(x))
                s = " ,".join(l)
            s_ = s.split(" ,")
            for y in s_:
                print("".join(y).strip("[]").replace(","," "))
        else:
            print("The operation cannot be performed.")
        print("\n")

def multiply_matrices():
        n,m = [int(x) for x in input("Enter size of first matrix: ").split()]
        matrix_a = []
        print("Enter first matrix:")
        for i in range(n):
            i_ = [int(x) if x.isdigit() else float(x) for x in input().split()]
            matrix_a.append(i_)
        n_,m_ = [int(x) for x in input("Enter size of second matrix: ").split()]
        matrix_b = []
        print("Enter second matrix:")
        for j in range(n_):
            j_ = [int(x) if x.isdigit() else float(x) for x in input().split()]
            matrix_b.append(j_)
        result = []
        for i in range(n):
            i_ = [0 for x in range(m_)]
            result.append(i_)

        if m == n_:

            for i in range(n):
                for k in range(n_):
                    for j in range(m_):
                        result[i][j] += matrix_a[i][k] * matrix_b[k][j]

            l = []
            s = ""
            print("The result is:")
            for x in result:
                l.append(str(x))
                s = " ,".join(l)
            s_ = s.split(" ,")
            for y in s_:
                print("".join(y).strip("[]").replace(","," "))
        else:
            print("The operation cannot be performed.")
        print("\n")

def transpose():
    user_choice = input("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: """)
    n,m = [int(x) for x in input("Enter size of matrix: ").split()]
    matrix_a = []
    print("Enter matrix:")
    for i in range(n):
        i_ = [int(x) if x.isdigit() else float(x) for x in input().split()]
        matrix_a.append(i_)
    result = []
    for i in range(m if user_choice == "1" or user_choice == "2" else n):
        i_ = [0 for x in range(n if user_choice == "1" or user_choice == "2" else m)]
        result.append(i_)
    for i in range(n):
        for j in range(m):
            if user_choice == "1":
                result[j][i] = matrix_a[i][j]
            elif user_choice == "2":
                result[(m-1)-j][(n-1)-i] = matrix_a[i][j]
            elif user_choice == "3":
                result[i][(m-1)-j] = matrix_a[i][j]
            elif user_choice == "4":
                result[(n-1)-i][j] = matrix_a[i][j]

    l = []
    s = ""
    print("The result is:")
    for x_ in result:
        l.append(str(x_))
        s = " ,".join(l)
    s_ = s.split(" ,")
    for y_ in s_:
        print("".join(y_).strip("[]").replace(",", " "))
    print("\n")


def matrix_minor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]




def det(m):
   #base case for 2x2 matrix
    if len(m) == 2:
        return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    elif len(m) == 1:
        return m[0][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c) * m[0][c] * det(matrix_minor(m,0,c))
    return determinant



def matrix_det():
        n,m = [int(x) for x in input("Enter size of matrix: ").split()]
        matrix_a = []
        print("Enter matrix:")
        for i in range(n):
            i_ = [int(x) if x.isdigit() else float(x) for x in input().split()]
            matrix_a.append(i_)
        print(f"The result is:\n{det(matrix_a)}")
        print("\n")




def inverse():
        n,m = [int(x) for x in input("Enter size of matrix: ").split()]
        matrix_a = []
        print("Enter matrix:")
        for i in range(n):
            i_ = [int(x) if x.isdigit() else float(x) for x in input().split()]
            matrix_a.append(i_)
        temp = []
        for i in range(n):
            i_ = [0 for x in range(m)]
            temp.append(i_)
        determinant = det(matrix_a)
        if n == 2:
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
        elif determinant == 0:
            print("This matrix doesn't have an inverse.")

        #find matrix of cofactors
        cofactors = []
        for r in range(n):
            cofactorRow = []
            for c in range(n):
                minor = matrix_minor(matrix_a,r,c)
                cofactorRow.append(((-1)**(r+c)) * det(minor))
            cofactors.append(cofactorRow)

        #transpose cofactor
        for i in range(n):
            for j in range(n):
                temp[j][i] = cofactors[i][j]

        for r in range(len(temp)):
            for c in range(len(temp)):
                temp[r][c] = round(temp[r][c]/determinant,3)



        l = []
        s = ""
        print("The result is:")
        for x_ in temp:
            l.append(str(x_))
            s = " ,".join(l)
        s_ = s.split(" ,")
        for y_ in s_:
            print("".join(y_).strip("[]").replace(",", " "))
        print("\n")







while True:


    user_choice = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: """)
    if user_choice == "0":
        break
    elif user_choice == "1":
        add_matrices()
    elif user_choice == "2":
        constant_x_matrix()
    elif user_choice == "3":
        multiply_matrices()
    elif user_choice == "4":
        transpose()
    elif user_choice == "5":
        matrix_det()
    elif user_choice == "6":
        inverse()

