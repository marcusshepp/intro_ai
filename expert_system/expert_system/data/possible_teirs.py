possible_teirs = {
    "bronze": range(0),
    "silver": range(0, 2),
    "gold": range(2, 4),
    "platinum": range(4, 6),
    "diamond": range(6, 8),
    "master": range(8, 10),
    "challenger": range(10, 12),
}

x = 4
for key in possible_teirs:
    if x in possible_teirs[key]:
        print key
