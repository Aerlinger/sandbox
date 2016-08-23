arr = [2, 11, 3, 5, 13, 7, 19, 17, 23]
inc = [0, 0 , 1, 1, 1 , 2, 2 , 3 , 3]

counts = dict([])


last_val = -1000
count = 0
start_idx = 0
end_idx = 0
cursor = 0

while cursor <= len(arr):
  if cursor < len(arr):
    cur_val = arr[cursor]
  else:
    cur_val = -1000

  if cur_val > last_val:
    last_val = cur_val
    count += 1
    end_idx = cursor
    cursor += 1

  else:
    if count > 0:
      counts[count] = (start_idx, end_idx)
      print "(%i, %i): %i" % (start_idx, end_idx, count)

    if cursor is len(arr):
      break
    else:
      start_idx = cursor
      end_idx = cursor
      last_val = -1000
      count = 0

print counts
