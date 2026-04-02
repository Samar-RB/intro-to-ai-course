from collections import Counter
from color_blocks_state import color_blocks_state

_goal_neighbor_pairs = set()
_goal_visible = []
_goal_count = Counter()

def init_goal_for_heuristics(goal_blocks):
    global  _goal_neighbor_pairs,_goal_visible, _goal_count
    if not goal_blocks:
        _goal_neighbor_pairs = set()
        _goal_visible = []
        _goal_count = Counter()
        return
    vals = [x.strip() for x in goal_blocks.split(",") if x.strip()]
    _goal_visible = list(map(int, vals))
    prs = set()
    for a, b in zip(_goal_visible, _goal_visible[1:]):
        if a <= b:
            prs.add((a, b))
        else:
            prs.add((b, a))
    _goal_neighbor_pairs = prs
    _goal_count = Counter(_goal_visible)

def _pair_matches_goal(b1, b2):
    v1, h1 = b1
    v2, h2 = b2
    for x, y in ((v1, v2), (v1, h2), (h1, v2), (h1, h2)):
        pair = (x, y) if x <= y else (y, x)
        if pair in _goal_neighbor_pairs:
            return True
    return False

def _missing_visibles(blocks):
    count_current = Counter(v for v, _ in blocks)
    total_missing = 0
    for val, required_amount in _goal_count.items():
        total_missing += max(0, required_amount - count_current.get(val, 0))
    return total_missing


def base_heuristic(_color_blocks_state):
    b = _color_blocks_state.blocks
    n = len(b)
    if n < 2:
        return 0
    s = 0
    for i in range(n - 1):
        if not _pair_matches_goal(b[i], b[i + 1]):
            s += 1
    return s

def advanced_heuristic(_color_blocks_state):
    blocks = _color_blocks_state.blocks
    n = len(blocks)

    if n == 0:
        return 0

    score = 0
    used = False

    for index, (left, right) in enumerate(zip(blocks[:-1], blocks[1:])):
        correct = _pair_matches_goal(left, right)

        if correct:
            if (not used
                and index < len(_goal_visible)
                and _goal_visible[index] not in left):
                score += 1
                used = True
        else:
            score += 1
            used = True

    score += _missing_visibles(blocks)
    return score


