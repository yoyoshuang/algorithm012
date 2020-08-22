学习笔记
# 双向bsf模版

front = {start_node}
back = {end_node}
level = 0
visited = {}
while front and back:
    level += 1
    next_front = []
    for node in front:
        if node in back:
            return 
        if node not in visited:
            next_front.append(node)
            visited.append(node)
    front = next_front
    if len(front)>len(back):
        front, back = back, front
return 