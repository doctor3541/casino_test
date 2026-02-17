
PAYLINES = [
    [(0,i) for i in range(5)],
    [(1,i) for i in range(5)],
    [(2,i) for i in range(5)],
    [(3,i) for i in range(5)],
    [(4,i) for i in range(5)],

    [(i,0) for i in range(5)],
    [(i,4) for i in range(5)],

    [(i,i) for i in range(5)],
    [(i,4-i) for i in range(5)],
]
