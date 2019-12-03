import heapq

first_wire = input().split(',')
second_wire = input().split(',')

def find_closest_point(first_wire, second_wire):
    visited = {}

    row, column = 0, 0
    for action in first_wire:
        move = action[0]
        times = int(action[1:])
        while times:
            if move == 'D':
                row += 1
            elif move == 'U':
                row -= 1
            elif move == 'R':
                column += 1
            elif move == 'L':
                column -= 1
            times -= 1
            visited[(row, column)] = 1

    row, column = 0, 0
    pq = []
    for action in second_wire:
        move = action[0]
        times = int(action[1:])
        while times:
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
                heapq.heappush(pq, abs(row) + abs(column))
    return heapq.heappop(pq)

print(find_closest_point(first_wire, second_wire))