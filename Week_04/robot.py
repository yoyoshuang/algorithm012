class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 北 东 南 西
        direc = [(0,1),(1,0), (0,-1), (-1,0)]
        px, py = 0,0
        di = 0
        maxd = 0
        pnots = []
        for i in range(len(obstacles)):
            pnot = (obstacles[i][0], obstacles[i][1])
            pnots.append(pnot)
        pnots = set(pnots)
        for step in commands:
            if step == -1:
                di = (di+1) % 4
            elif step == -2:
                di = (di-1) % 4
            
            else:
                for i in range(step):
                    dx, dy = direc[di]
                    next_x = px + dx
                    next_y = py + dy
                    if (next_x, next_y) not in pnots:
                        px = px+dx
                        py = py+dy 
                        # print(px, py)
                        maxd = max(maxd, px*px+py*py)
        return maxd