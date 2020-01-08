def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        sum_total = 0
        for x in range(begin_number, end_number+1, step):
            sum_total += x
        return sum_total

print(sequence_sum(1, 5, 3))
print(sequence_sum(2, 1, 3))
