

# We can find a generic formula for S(2n) and S(2n+1)
# S(2n+1) = 4a(1) - 3a(n+1) and S(2n) = 4a(1) - a(n)

def get_nth_term(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2*get_nth_term(n//2)
    else:
        return get_nth_term((n-1)//2) - 3*get_nth_term((n-1)//2+1)

def get_sum(n):
    if n % 2 == 0:
        return 4*get_nth_term(1) - get_nth_term(n//2)
    else:
        return 4*(get_nth_term(1)) - 3*get_nth_term((n-1)//2 + 1)

print(get_sum(10**12)) 





