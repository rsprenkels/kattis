if __name__ == '__main__':
    _ = input()
    need_to_learn = list(map(int, input().split()))
    already_leanred = list(map(int, input().split()))
    print([k for k in need_to_learn if k not in already_leanred][0])

# from 562.1 rank 874 (team 309.8 rank 165)
