import numpy as np

N = 60
np.random.seed(42)
scales = np.random.uniform(0.3, 1.0, N)

# initialize in a spiral just to have a good starting point
cx = np.zeros(N)
cy = np.zeros(N)
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
coords = hex_spiral(N)
for i in range(N):
    cx[i] = np.sqrt(3) * (coords[i][0] + coords[i][1]/2) * 0.5
    cy[i] = 1.5 * coords[i][1] * 0.5

# physics
dt = 0.5
for step in range(300):
    for i in range(N):
        for j in range(i+1, N):
            dx = cx[i] - cx[j]
            dy = cy[i] - cy[j]
            dist = np.hypot(dx, dy)
            target = (np.sqrt(3)/2) * (scales[i] + scales[j]) * 1.02 # 2% gap
            if dist < target:
                overlap = target - dist
                cx[i] += (dx/dist) * overlap * 0.5
                cx[j] -= (dx/dist) * overlap * 0.5
            elif dist > target and dist < target * 1.5:
                # pull together
                gap = dist - target
                cx[i] -= (dx/dist) * gap * 0.05
                cx[j] += (dx/dist) * gap * 0.05

print("Physics done. Dist min:", np.hypot(cx[0]-cx[1], cy[0]-cy[1]))
