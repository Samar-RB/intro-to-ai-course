import math
h = None

def alphabeta_max_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    return maximin(current_game, depth, -math.inf, math.inf)


def alphabeta_min_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    return minimax(current_game, depth, -math.inf, math.inf)


def maximin(current_game, depth, alpha_val=-math.inf, beta_val=math.inf):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v, best_move = -math.inf, None
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move, depth - 1, alpha_val, beta_val)
        if v < mx:
            v, best_move = mx, move
        alpha_val = v if v > alpha_val else alpha_val
        if alpha_val >= beta_val:
            break
    return v, best_move


def minimax(current_game, depth, alpha_val=-math.inf, beta_val=math.inf):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v, best_move = math.inf, None
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move, depth - 1, alpha_val, beta_val)
        if v > mx:
            v, best_move = mx, move
        beta_val = v if v < beta_val else beta_val
        if alpha_val >= beta_val:
            break
    return v, best_move
