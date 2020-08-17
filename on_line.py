#Checks to see if a point is on a given line.
def on_line(line, point):
    x = point[0]
    y = point[1]
    print(line['x1'])
    m = (line['y2'] - line['y1'])/(line['x2'] - line['x1'])
    b = line['y1'] - m*line['x1']
    if y == m*x + b:
        return True
    return False
l1 = {'x1': 1, 'y1':1, 'x2': 3, 'y2': 2}
p1 = (5, 9)
print(on_line(l1, p1))
