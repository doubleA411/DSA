"""
Question - 2 
The first line of input will contain an integer n (1 ≤ n ≤ 105), the number of events. 
The next line will contain n space-separated integers. 
If the integer is -1 then it means a crime has occurred. Otherwise, the integer will be positive, 
the number of officers recruited together at that time. No more than 10 officers will be recruited at a time. 
"""



events = int(input("Enter number of events :"))
event_list  = []
for i in range(0,events):
    event = int(input())
    event_list.append(event)
print(event_list)
unsolved_case = 0;
police = 0
for eve in event_list:
    if(eve == -1):
        if(police > 0):
            police=police-1
        else:
            unsolved_case= unsolved_case + 1
    else:
        police = police + eve
print("unsolved cases:",unsolved_case)
print("no. of police",police)