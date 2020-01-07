'''
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a list of meetings that will happen during a day, \
    find the minimum number of meeting rooms that can fit all meetings.

Each meeting will be represented by a tuple of (start_time, end_time), 
where both start_time and end_time will be represented by an integer to indicate the time. 
start_time will be inclusive, and end_time will be exclusive, meaning a meeting of (0, 10) and (10, 20) \
    will only require 1 meeting room.

Here's some examples and some starting code:
'''

def meeting_rooms(meetings):
  
  stack_of_rooms = sorted(meetings, key = lambda x:(x[0], x[1])) # stack rooms
  count_rooms = 0
  while stack_of_rooms:
    flag = -1
    available = []
    for i, interval in enumerate(stack_of_rooms):

      if interval[0] >= flag:
        available.append(i)
        flag = interval[1]
    
    for j in available[::-1]:
      stack_of_rooms.pop(j)

    count_rooms += 1

  return count_rooms

# print 1
print(meeting_rooms([(0, 10), (10, 20)]))
# 1

# 10/2 = 5
# 30/2 = 15
# 40/2 = 20

print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
# 3 (all meetings overlap at time 20)

# 50/2 = 25
# 31/2 = 15
# 50/2 = 25


# 5 15 --> 5 ok , 15 ok, pop 15