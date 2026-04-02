import heapq
from search_node import search_node
from color_blocks_state import color_blocks_state

def create_open_set():
    return ([], {})

def create_closed_set():
    return {}

def add_to_open(vn, open_set):
    priority_q, node_map = open_set
    heapq.heappush(priority_q, vn)
    node_map[vn.state] = vn

def open_not_empty(open_set):
    priority_q, _ = open_set
    return bool(priority_q)

def get_best(open_set):
    priority_q, node_map = open_set
    while priority_q:
        n = heapq.heappop(priority_q)
        if node_map.get(n.state) is n:
            del node_map[n.state]
            return n
    return None

def add_to_closed(vn, closed_set):
    closed_set[vn.state] = vn

def duplicate_in_open(vn, open_set):
    priority_q, node_map = open_set
    exist = node_map.get(vn.state)
    if exist is None:
        return False
    if exist.g <= vn.g:
        return True
    node_map[vn.state] = vn
    heapq.heappush(priority_q, vn)
    return False

def duplicate_in_closed(vn, closed_set):
    exist = closed_set.get(vn.state)
    if exist is None:
        return False
    if exist.g <= vn.g:
        return True
    del closed_set[vn.state]
    return False

def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.get_state_str()) 

def search(start_state, heuristic):
    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, g=0,h=heuristic(start_state),prev=None)
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):
        current = get_best(open_set)
        if current is None:
            break
        if color_blocks_state.is_goal_state(current.state):
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path
        add_to_closed(current, closed_set)

        for neighbor,edge_cost in current.get_neighbors():
            new_g = current.g + edge_cost
            new_h = heuristic(neighbor)
            curr_neighbor = search_node(neighbor, g=new_g, h=new_h, prev=current)
            if duplicate_in_open(curr_neighbor, open_set):
                continue
            if duplicate_in_closed(curr_neighbor, closed_set):
                pass
            add_to_open(curr_neighbor, open_set)
    return None
