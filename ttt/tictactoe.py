# board

# 1 2 3
# 4 5 6 => 1 2 3 4 5 6 7 8 9
# 7 8 9

import math
import random
import copy


all_positions = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Winning:
winning_positions = set([
(1, 4, 7),
(2, 5, 8),
(3, 6, 9),

(1, 5, 9),
(7, 5, 3),

(1, 2, 3),
(4, 5, 6),
(7, 8, 9)
])


starter_player = "A"

def player_won(player_positions, player="X"):
  my_positions = player_positions[player]

  for winning_position in winning_positions:
    if set(winning_position).issubset(set(my_positions)):
      return True

  return False

def game_tied(player_positions):
  return len(available_moves(player_positions)) == 0

def available_moves(player_positions):
  return all_positions - (set(player_positions["X"]) | set(player_positions["O"]))

def coords_to_position(i, j):
  if i > 3 or i < 1 or j > 3 or j < 1:
    raise Exception("coords (%s, %s) are out of bounds!" % (i, j))

  return i + 3*(j-1)

def position_to_coords(pos):
  if pos > 9 or pos < 1:
    raise Exception("position %s is out of bounds!" % pos)

  return ((pos - 1) % 3 + 1, math.ceil(pos / 3))

def draw_board(player_positions):
  playerX_positions = player_positions["X"]
  playerO_positions = player_positions["O"]

  buffer = ""

  for j in range(1, 4):
    # buffer += ' ' * i
    for i in range(1, 4):
      if coords_to_position(i, j) in playerX_positions:
        token = "X"
      elif coords_to_position(i, j) in playerO_positions:
        token = "O"
      else:
        token = "-"

      buffer += " %2s " % token
    buffer += "\n"

  return buffer


def other_player(player_token):
  if player_token == "X":
    return "O"
  else:
    return "X"

def make_move(player_positions, position, player = "X", doprint = True):
  # if position in player_positions[player]:
  #   raise Exception("Position %s is not a legal move because it has already been played!"% position)

  # print(position, player_positions, player)

  new_move =  player_positions[player] | set([position])
  opponent = other_player(player)

  new_board_state = {
    player: new_move,
    opponent: player_positions[opponent]
  }

  if doprint:
    print(player + " moved to ", position_to_coords(position))
    print(draw_board(new_board_state))

  return new_board_state

def make_random_move(player_positions, player = "O", doprint=True):
  random_position = random.sample(available_moves(player_positions), 1)[0]

  return make_move(player_positions, random_position, player, doprint)


def determine_best_move(player_positions, my_player = "X"):
  results = simulate_move(player_positions, my_player)

  best_score = max(results.keys())
  best_move = results[best_score]

  return {"best_move": best_move, "best_score": best_score}

def merge_dict(left, right):
  # for k, v in left.items():
  #   right.setdefault(k, []).extend(v)

  # return right

  return left

def simulate_move(player_positions, player = "X", move_history = [], doprint=False):
  if player_won(player_positions, "X"):
    print("\tX WIN", (9-len(move_history), move_history))
    return (9-len(move_history), move_history)

  if player_won(player_positions, "O"):
    print("\tO WIN", (-9+len(move_history), move_history))
    return (-9+len(move_history), move_history)

  if game_tied(player_positions):
    print("\tTIE", move_history, "\n")
    return (0, move_history)

  num_available_moves = len(available_moves(player_positions))

  max_score = -1000
  current_history = None

  for available_move in available_moves(player_positions):
    updated_player_position = make_move(player_positions, available_move, player, doprint=doprint)
    score, history  = simulate_move(updated_player_position, other_player(player), move_history + [available_move])

    if score > max_score:
      max_score = score
      current_history = history

  print("Best scores for move", max_score, " --> ", (current_history))
  return (max_score, current_history)


merged = merge_dict({"a": [], "b": [1, 2 ,3]}, {"a": [1], "b": [3, 4], "c": [1, 10], "d": []})

def test_coords():
  for i in range(1, 4):
    for j in range(1, 4):
      print(i, j, position_to_coords(coords_to_position(i, j)))

  for i in range(1, 10):
    x, y = position_to_coords(i)

    print(i, coords_to_position(x, y))

player_positions = {
  "X": set([]),
  "O": set([])
}

current_turn = "X"
turn = 1

while(False):
  if current_turn == "X":
    best_move = determine_best_move(player_positions, "X")
    move = best_move["best_move"]

    if type(move) == list:
      move = move[0]

    player_positions = make_move(player_positions, move, "X")

  else:
    player_positions = make_random_move(player_positions, player="O")

  if player_won(player_positions, current_turn):
    print("PLAYER ", current_turn, " has won on turn %s!" % turn)
    break

  elif game_tied(player_positions):
    print("TIE ", current_turn, " on turn %s" % turn)

  current_turn = other_player(current_turn)

  turn += 1

# print(best_move)

# player_positions = make_move(player_positions, 3, "X")
# player_positions = make_move(player_positions, 2, "O")

def predict_best_move(player_positions, player = "X"):
  score, history = simulate_move(player_positions, player)
  print("Best Move for ", player, ":", (score, history))

  # if player == "X":
  #   return (X_max, X_move_history)
  # else:
  #   return (O_min, O_move_history)

player_positions = {
  "X": set([3, 4, 7]),
  "O": set([1, 2])
}

# print(draw_board(player_positions))
# print("STARTING AS O")
# print("BEST MOVE", predict_best_move(player_positions, "O"))

# print("STARTING AS X")
# print("BEST MOVE", predict_best_move(player_positions, "X"))

player_positions = {
  "X": set([3, 7, 8]),
  "O": set([1, 2])
}

print(draw_board(player_positions))
print("STARTING AS O")
print("BEST MOVE", predict_best_move(player_positions, "O"))

print("STARTING AS X")
print("BEST MOVE", predict_best_move(player_positions, "X"))


player_positions = {
  "X": set([1, 5]),
  "O": set([2, 3, 4, 7])
}

print(draw_board(player_positions))
print("STARTING AS O")
print("BEST MOVE", predict_best_move(player_positions, "O"))

print("STARTING AS X")
print("BEST MOVE", predict_best_move(player_positions, "X"))


# print(draw_board(player_positions))

# print("STARTING AS O")
# print("BEST MOVE", predict_best_move(player_positions, "O"))
#
# print("STARTING AS X")
# print("BEST MOVE", predict_best_move(player_positions, "X"))

player_positions = {
  "X": set([1, 2, 5]),
  "O": set([3, 4, 7])
}

# print(draw_board(player_positions))

# print("BEST MOVE", predict_best_move(player_positions, "O"))
# print("BEST MOVE", predict_best_move(player_positions, "X"))

player_positions = {
  "X": set([1, 5]),
  "O": set([3, 7])
}

# print(draw_board(player_positions))

# print("BEST MOVE", predict_best_move(player_positions, "O"))
# print("BEST MOVE", predict_best_move(player_positions, "X"))


#
# current_turn = "X"
# turn = 1
#
#
# while(False):
#   if current_turn == "X":
#     best_move = determine_best_move(player_positions, "X")
#     move = best_move["best_move"]
#
#     if type(move) == list:
#       move = move[0]
#
#     player_positions = make_move(player_positions, move, "X")
#
#   else:
#     player_positions = make_random_move(player_positions, player="O")
#
#   if player_won(player_positions, current_turn):
#     print("PLAYER ", current_turn, " has won on turn %s!" % turn)
#     break
#
#   elif game_tied(player_positions):
#     print("TIE ", current_turn, " on turn %s" % turn)
#
#   current_turn = other_player(current_turn)
#
#   turn += 1
#
#
#
