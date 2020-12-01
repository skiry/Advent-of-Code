import heapq

first_wire = input().split(',')
second_wire = input().split(',')

def find_minimum_steps(first_wire, second_wire):
    visited = {}

    row, column = 0, 0
    steps = 0
    for action in first_wire:
        move = action[0]
        times = int(action[1:])
        while times:
            steps += 1
            if move == 'D':
                row += 1
            elif move == 'U':
                row -= 1
            elif move == 'R':
                column += 1
            elif move == 'L':
                column -= 1
            times -= 1
            if not (row, column) in visited:
                visited[(row, column)] = steps

    row, column = 0, 0
    pq = []
    steps = 0
    for action in second_wire:
        move = action[0]
        times = int(action[1:])
        while times:
            steps += 1
            if move == 'D':
                row += 1
            elif move == 'U':
                row -= 1
            elif move == 'R':
                column += 1
            elif move == 'L':
                column -= 1
            times -= 1
            if (row, column) in visited:
                heapq.heappush(pq, steps + visited[(row, column)])
    return heapq.heappop(pq)

print(find_minimum_steps(first_wire, second_wire))