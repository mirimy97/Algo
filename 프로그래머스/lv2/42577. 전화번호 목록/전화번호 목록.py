

def solution(phone_book):
    phone_book.sort()
    N = len(phone_book)
    for i in range(N-1):
        is_same = True
        for pair in zip(phone_book[i], phone_book[i+1]):
            if pair[0] != pair[1]:
                is_same = False
                break
        if is_same:
            return False
    return True