def _calc_seat_id(row):
    row = row.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
    return int(row[:7], 2) * 8 + int(row[7:10], 2)

def find_seat_ids(filename):
    ids = sorted(_calc_seat_id(row) for row in open(filename))
    skip_check = ids[0]
    for id_ in ids:
        if (skip_check := skip_check + 1) == id_:
            break
    return ids[-1], id_ - 1

# 5.1, 5.2
print(find_seat_ids('day5/input.txt'))
