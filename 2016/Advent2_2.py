def move_up(start):
    result = start - 3
    if (start == 7 or start == 4 or start == 1):
        if (result < 1) : result = 1 
    elif (start ==  8 or start == 5 or start == 2):
        if (result<2): result = 2
    else:
        if (result<3): result = 3
    return result
def move_down(start):
    result = start + 3
    if (start == 1 or start == 4 or start == 7):
        if (result > 7) : result = 7
    elif (start == 2 or start == 5 or start == 8):
        if (result>8): result = 8
    else:
        if (result>9): result = 9
    return result
def move_left(start):
    result = start - 1
    if (start == 3 or start ==2 or start ==1):
        if (result < 1) : result = 1
    elif (start == 6 or start == 5 or start == 4):
        if (result<4): result = 4
    else:
        if (result<7): result = 7
    return result
def move_right(start):
    result = start + 1
    if (start == 1 or start == 2 or start == 3):
        if (result > 3) : result = 3
    elif (start == 4 or start== 5 or start == 6):
        if (result>6): result = 6
    else:
        if (result>9): result = 9
    return result

def new_move_up(start):
    if (start == '1' or start == '2' or start == '4' or start == '5' or start == '9') : return start
    if (start == '3'): return '1'
    if (start == '8' or start == '6' or start == '7'): return str(int(start)-4)
    if (start == 'A') : return '6'
    if (start == 'B') : return '7'
    if (start == 'C') : return '8'
    if (start == 'D') : return 'B'
def new_move_down(start):
    if (start == 'D' or start == 'A' or start == 'C' or start == '5' or start == '9') : return start  
    if (start == 'B'): return 'D'
    if (start == '6'): return 'A'
    if (start == '8'): return 'C'
    if (start == '7'): return 'B'
    if (start == '2' or start == '3' or start =='4'): return str(int(start)+4)
    if (start == '1'): return '3'
def new_move_right(start):
    if (start == 'D' or start == 'C' or start == '9' or start == '4' or start == '1') : return start
    if (start == '5' or  start == '6' or start == '7' or start == '8' or start == '2' or start == '3'): return str(int(start)+1)
    if (start =='B'): return 'C'
    if (start == 'A'): return 'B'
def new_move_left(start):
    if (start == 'D' or start == 'A' or start == '5' or start == '2' or start == '1') : return start
    if (start == '6' or  start == '7' or start == '8' or start == '9' or start == '3' or start == '4'): return str(int(start)-1)
    if (start =='B'): return 'A'
    if (start == 'C'): return 'B'
    
# with open('input2_es2.txt') as file:
#     starting_point = 5
#     combination = []
#     for row in file.readlines():
#         print("STARTING ROW NUMBER :  " + str(starting_point))
#         for char in row:
#             print("COMMAND : " + char)
#             if char == "U":
#                 starting_point=move_up(starting_point)
#                 #print("move up:  " + str(starting_point))
#             elif char == "D":
#                 starting_point=move_down(starting_point)
#                 #print("move down:  " + str(starting_point))
#             elif char == "L":
#                 starting_point=move_left(starting_point)
#                 #print("move left:  " + str(starting_point))
#             elif char == "R":
#                 starting_point=move_right(starting_point)
#                 #print("move right:  " + str(starting_point))
#         combination.append(starting_point)
#         print("END ROW NUMBER : " + str(starting_point))
#     print("COMBINAZIONE : " + str(combination))

with open('input2_es2.txt') as file:
    starting_point = '5'
    combination = []
    for row in file.readlines():
        print("STARTING ROW NUMBER :  " + str(starting_point))
        row =row.replace(r' ',r'')
        for char in row:
            print("COMMAND : " + char)
            if char == "U":
                starting_point=new_move_up(starting_point)
                print("move up:  " + str(starting_point))
            elif char == "D":
                starting_point=new_move_down(starting_point)
                print("move down:  " + str(starting_point))
            elif char == "L":
                starting_point=new_move_left(starting_point)
                print("move left:  " + str(starting_point))
            elif char == "R":
                starting_point=new_move_right(starting_point)
                print("move right:  " + str(starting_point))
        combination.append(starting_point)
        print("END ROW NUMBER : " + str(starting_point))
    print("COMBINAZIONE : " + str(combination))

# import sys
# 
# PAD = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]
#        ]
# 
# cur = (1, 1)  # start at '5'
# 
# INSTR = {"U": (0, -1), "D": (0, 1),
#          "L": (-1, 0), "R": (1, 0),
#          }
# file =open('input2_es2.txt')
# for line in file:
#     for d in line.strip():
#         cur = (max(0, min(cur[0] + INSTR[d][0], 2)),
#                max(0, min(cur[1] + INSTR[d][1], 2)))
#     print (PAD[cur[1]][cur[0]])