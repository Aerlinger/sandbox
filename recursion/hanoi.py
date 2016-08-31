#
#     |            |             |
#     |            |             |
#     |            |             |
#     |            |             |
# ------------------------------------
#     A            B             C

import copy

# stack(start, dest, temp)

# 1: A -> B

# MOV(C -> B) # Start: A, Dest: B, Temp: C
#  A -> C
#  A -> B  *
#  C -> B

# 3 - Start: A, Dest: B, Temp: C
# A -> B
# A -> C
# B -> C
# A -> B  *
# MOV(C -> B)

def mov(start, dest, temp):
  print(start, dest, temp)

  new_start = start - 1
  new_dest = dest + 1

  if start == 1:
    print("BASE: Move start to dest")
    return

  mov(new_start, temp, new_dest)
  mov(new_dest, temp, new_start)

mov(2, 0, 0)
