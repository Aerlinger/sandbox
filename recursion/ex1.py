class Fibo(object):
  def __init__(self):
    print("I have been created")

  def fib(self, n):
    if n == 0:
      return 0
    if n == 1:
      return 1
    else:
      return self.fib(n - 1) + self.fib(n - 2)

  def whatAmI(self, passMyInstance):
    print(self == passMyInstance)


def permute(arr):
  if len(arr) == []:
    return []

  permutations = []



  for idx in range(len(arr)):
    prefix = arr[:(idx)]
    suffix = arr[(idx+1):]
    item = arr[idx]

    j

    print(result)
    print(prefix)
    print([item])
    print(suffix)
    print()

    permutations += result

    # print(result)

  return permutations


def permute(arr):
  permutations = []

  for idx in range(len(arr)):
    prefix = arr[:(idx)]
    suffix = arr[(idx + 1):]
    item = arr[idx]

    result = [item, *(prefix + suffix)]

    permutations += [result]

  return permutations


def permute_wrapper(arr):
  if len(arr) == 1:
    return arr

  arr = permute(arr)

  permutations = []

  for item in arr:
    first = item[0]
    rest = item[1:]
    tail = permute_wrapper(rest)

    print(first, tail)

    permutations += first, permute_wrapper(rest)

  return permutations



print(permute(["A", "B", "C"]))
print(permute_wrapper(["A", "B", "C"]))



# print(permute(["A"]))
# print(print_permutations(["A", "B", "C", "D"]))




