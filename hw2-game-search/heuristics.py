from game_state import game_state

def base_heuristic(curr_state):
    grid = curr_state.get_grid()
    loc1, loc2 = curr_state.get_player_locations()[1], curr_state.get_player_locations()[2]
    player1_state = game_state(grid.copy(), loc1, loc2, 1)
    p1_moves = len(player1_state.potential_moves())
    player2_state = game_state(grid.copy(), loc1, loc2, 2)
    p2_moves = len(player2_state.potential_moves())
    v = p1_moves - p2_moves
    return v


def advanced_heuristic(curr_state):
    return 0
