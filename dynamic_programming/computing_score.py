possible_scores = [2, 3, 7]

def compute_score(total_score, scores=[]):
  if (sum(scores) == total_score):
    print(scores)
    return total_score

  if (sum(scores) > total_score):
    return total_score

  for score in possible_scores:
    return total_score + compute_score(total_score, scores + [score])



compute_score(12)
compute_score(1)

for num in range(100):
  # print(compute_score(num) > 0)

  print compute_score(num)
  # print(num)

