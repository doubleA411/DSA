sums = 8
matchsticks = 0
str_sum = str(sums)

for i in str_sum:
    if i == "1" in str_sum:
        matchsticks = matchsticks+ 2
    elif  i == "2" or i=="3" or i=="5" in str_sum:
        matchsticks = matchsticks+ 5
    elif i == "9" or i=="6" or i=="0" in str_sum:
        matchsticks = matchsticks + 6
    elif i == "7" in str_sum:
        matchsticks = matchsticks + 3
    elif i == "4" in str_sum:
        matchsticks = matchsticks + 4
    elif i == "8" in str_sum:
        matchsticks = matchsticks+ 7
print(matchsticks)

# 2,3,5 - 5
# 9,6,0 - 6
# 4 - 4
# 7 - 3
# 1 - 2
# 8 - 7