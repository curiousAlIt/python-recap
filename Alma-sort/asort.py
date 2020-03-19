#
# Alma's sorting algorithm
#

def add_into_sorted(A, p):

    curr_ind = 0
    n = len(A)
    B = [None] * (n + 1)

    while curr_ind < n and p >= A[curr_ind]:
        B[curr_ind] = A[curr_ind]
        curr_ind += 1

    B[curr_ind] = p

    for j in range(curr_ind + 1, n + 1):
        B[j] = A[j - 1]

    return B

if __name__=='__main__':

    L = [2, 4, 5, 8]

    B = add_into_sorted(L, 4)

    print(f'Original L: {L}')
    print(f'After calling: {B}')
