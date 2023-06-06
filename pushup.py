sets = []

for i in range(4):
    pushup = int(input())
    sets.append(pushup)

final_res = 0

for set in sets:
    if set >= 20:
        final_res = final_res + 1
    

print(final_res)