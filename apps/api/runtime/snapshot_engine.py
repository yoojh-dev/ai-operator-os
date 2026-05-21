import copy


class SnapshotEngine:

    def __init__(self):

        self.snapshots = {}

    def save(self, trace_id: str, state):

        self.snapshots[trace_id] = copy.deepcopy(state)

    def load(self, trace_id: str):

        return self.snapshots.get(trace_id)