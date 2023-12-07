def stampaj_tabelu(mat):
    niz = ["A", "B", "C", "D", "E", "F", "G", "H"]
    print("   ", end="")
    for i in range(1, 9):
        print(i, end="")
        print("  ", end="")
    print("")
    for i in range(0, 8):
        for j in range(2, -1, -1):
            if j == 1:
                print(niz[i] + " ", end="")
            else:
                print("  ", end="")
            for k in range(0, 8):
                stampaj_pomocna(i, j, k, mat)
            print("")


def stampaj_pomocna(i, j, k, mat):
    pom_niz = [0, 1, 2]
    pom_niz = list(map(lambda x: x + 3*j, pom_niz))
    if (i + k) % 2 == 0:
        if len(mat[i][k]) >= pom_niz[0] + 1:
            print(mat[i][k][pom_niz[0]], end="")
        else:
            print(".", end="")
        if len(mat[i][k]) >= pom_niz[1] + 1:
            print(mat[i][k][pom_niz[1]], end="")
        else:
            print(".", end="")
        if len(mat[i][k]) == pom_niz[2] + 1:
            print(mat[i][k][pom_niz[2]], end="")
        else:
            print(".", end="")
    else:
        print("   ", end="")