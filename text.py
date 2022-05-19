def descending_order(num):
    # Bust a move right here
    l = [int(i) for i in str(num)]
    ordered = ''
    n = [*l]
    for i in n:
        mx = max(l)
        ordered += str(mx)
        l.remove(mx)
    return int(ordered)

descending_order(51)