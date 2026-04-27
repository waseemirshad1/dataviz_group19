def hex_spiral(n):
    coords = [(0,0)]
    if n <= 1: return coords
    
    directions = [(1,0), (0,1), (-1,1), (-1,0), (0,-1), (1,-1)]
    q, r = 0, 0
    radius = 1
    while len(coords) < n:
        q += directions[4][0]
        r += directions[4][1]
        for i in range(6):
            for _ in range(radius):
                if len(coords) < n:
                    coords.append((q, r))
                q += directions[i][0]
                r += directions[i][1]
        radius += 1
    return coords

print(len(hex_spiral(60)))
