import math

def alphabeta_max(current_game):
    return maximin(current_game, -math.inf, math.inf)


def alphabeta_min(current_game):
    return minimax(current_game, -math.inf, math.inf)


def maximin(current_game, alpha_val=-math.inf, beta_val=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v, best_move = -math.inf, None
    for move in current_game.get_moves():
        mx, next_move = minimax(move, alpha_val, beta_val)
        if v < mx:
            v, best_move = mx, move
        alpha_val = v if v > alpha_val else alpha_val
        if alpha_val >= beta_val:
            break
    return v, best_move


def minimax(current_game, alpha_val=-math.inf, beta_val=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v, best_move = math.inf, None
    for move in current_game.get_moves():
        mx, next_move = maximin(move, alpha_val, beta_val)
        if v > mx:
            v, best_move = mx, move
        beta_val = v if v < beta_val else beta_val
        if alpha_val >= beta_val:
            break
    return v, best_move
