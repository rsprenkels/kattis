import math

def retire_at(b: int, b_retire: int, b_save: int, a: int, a_save: int) -> int:
    b_total_saving = (b_retire - b) * b_save
    age_equal =  a + math.ceil(b_total_saving / a_save)
    if (age_equal - a) * a_save == b_total_saving:
        return age_equal + 1
    else:
        return age_equal

assert retire_at(b=20, b_retire=25, b_save=5, a=20, a_save=10) == 23

assert retire_at(b=20, b_retire=25, b_save=5, a=20, a_save=5) == 26

print(retire_at(*list(map(int, input().split()))))

# from 390.0 rank 957 to 392.6 rank 952
