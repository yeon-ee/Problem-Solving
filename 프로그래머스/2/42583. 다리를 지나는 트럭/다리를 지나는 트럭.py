from collections import deque
class Truck:
    def __init__(self, weight, bridge_length):
        self.weight = weight
        self.location = 1
        self.bridge_length = bridge_length

    def go(self):
        if self.location >= self.bridge_length:
            return self.weight
        else:
            self.location += 1
            return 0
        

def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = deque(truck_weights)
    bridge = deque()
    curr_weight = 0
    while len(trucks) > 0 or len(bridge) > 0:
        time += 1
        pop_bridge = False
        for truck in bridge:
            signal = truck.go()
            if signal != 0:
                curr_weight -= signal
                pop_bridge = True
        if pop_bridge:
            bridge.popleft()
        if len(trucks) > 0:
            if curr_weight + trucks[0] <= weight:
                truck_weight = trucks.popleft()
                T = Truck(truck_weight, bridge_length)
                curr_weight += truck_weight
                bridge.append(T)
    return time