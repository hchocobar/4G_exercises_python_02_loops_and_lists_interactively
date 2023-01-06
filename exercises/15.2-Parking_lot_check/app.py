def get_parking_lot(parking):
    available = 0
    occupied = 0
    for i in parking:
        available += i.count(2)
        occupied += i.count(1)
    state = {'total_slots': available + occupied,
             'available_slots': available,
             'occupied_slots': occupied}
    return state


parking_state = [[1, 1, 1],
                 [0, 0, 0],
                 [1, 1, 2]]
print(get_parking_lot(parking_state))
