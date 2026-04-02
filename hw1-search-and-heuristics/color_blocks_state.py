goalv_forsearch = []

def init_goal_for_search(goal_blocks):
    global goalv_forsearch
    if not goal_blocks:
        goalv_forsearch = []
        return ""
    cleaned_goalv_forsearch = [x.strip() for x in goal_blocks.split(",") if x.strip()]
    goalv_forsearch = list(map(int, cleaned_goalv_forsearch))

class color_blocks_state:
    
    def __init__(self, blocks_str=None, **kwargs):
        if "blocks" in kwargs and kwargs["blocks"] is not None:
            self._blocks = [tuple(b) for b in kwargs["blocks"]]
        else:
            self._blocks = self._parse(blocks_str)
        self._flat = tuple(self._blocks)

    @staticmethod
    def _parse(text):
        if not text:
            return []
        t = text.replace(" ", "")
        if not t:
            return []
        if ")" in t:
            parts = t.split("),")
            out = []
            for seg in parts:
                if seg.startswith("("):
                    seg = seg[1:]
                if seg.endswith(")"):
                    seg = seg[:-1]
                if seg:
                    x, y = seg.split(",")
                    out.append((int(x), int(y)))
            return out
        nums = [p for p in t.split(",") if p]
        return [(int(nums[i]), int(nums[i + 1])) for i in range(0, len(nums), 2)]

    @staticmethod
    def is_goal_state(_color_blocks_state):
        return [v for (v, _) in _color_blocks_state._blocks] == goalv_forsearch

    def get_neighbors(self):
        res = []
        n = len(self._blocks)

        for i in range(n):
            x, y = self._blocks[i]
            if x != y:  
                new_blocks = list(self._blocks)
                new_blocks[i] = (y, x)
                res.append((color_blocks_state(blocks=new_blocks), 1))
            
        for size in range(2, n + 1):
            cut = n - size
            prefix = self._blocks[:cut]
            suffix = self._blocks[cut:]
            new_state = list(prefix) + list(reversed(suffix))
            res.append((color_blocks_state(blocks=new_state), 1))

        return res

    def __hash__(self):
        return hash(self._flat)

    def __eq__(self, other):
        if not isinstance(other, color_blocks_state):
            return False
        return self._flat == other._flat

    def get_state_str(self):
        parts = []
        for x, y in self._blocks:
            parts.append("({},{})".format(x, y))
        return ",".join(parts)


    @property
    def blocks(self):
        return list(self._blocks)
