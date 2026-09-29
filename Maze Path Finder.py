import cv2
from collections import deque
def get_image():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("      Maze Path Finder")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    path = input("Enter maze image path: ")
    return cv2.imread(path)
def gray(image):
    print("turning into grayscale")
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def black_white(image):
    print("turning into black and white")
    value, result = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
    return result
def count_pixels(image):
    black = 0
    white = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == 0:
                black += 1
            else:
                white += 1
    print("Black pixels:", black)
    print("White pixels:", white)
def maze_boundary(image, binary):
    print("Finding maze boundary...")
    contours, x = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    result = image.copy()
    if len(contours) == 0:
        print("Boundary not found")
        return result
    biggest = contours[0]
    for c in contours:
        if cv2.contourArea(c) > cv2.contourArea(biggest):
            biggest = c
    cv2.drawContours(result, [biggest], -1, (0, 0, 255), 3)
    print("Maze boundary found")
    return result
def find_points(image, binary):
    print("Finding start and end points...")
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    blue1 = (90, 80, 50)
    blue2 = (140, 255, 255)
    blue = cv2.inRange(hsv, blue1, blue2)
    contours, x = cv2.findContours(
        blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    start = None
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        m = cv2.moments(c)
        if m["m00"] != 0:
            x = int(m["m10"] / m["m00"])
            y = int(m["m01"] / m["m00"])
            for i in range(y, len(binary)):
                if binary[i][x] == 255:
                    start = (i, x)
                    break
    red1 = cv2.inRange(
        hsv, (0, 80, 50), (10, 255, 255)
    )
    red2 = cv2.inRange(
        hsv, (170, 80, 50), (180, 255, 255)
    )
    red = cv2.bitwise_or(red1, red2)
    contours, x = cv2.findContours(
        red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    end = None
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        m = cv2.moments(c)
        if m["m00"] != 0:
            x = int(m["m10"] / m["m00"])
            y = int(m["m01"] / m["m00"])
            for i in range(y, -1, -1):
                if binary[i][x] == 255:
                    end = (i, x)
                    break
    print("Start:", start)
    print("End:", end)
    return start, end
def solve(binary, start, end):
    print("Solving maze...")
    rows = len(binary)
    cols = len(binary[0])
    visited = [[False] * cols for i in range(rows)]
    parent = [[None] * cols for i in range(rows)]
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while q:
        current = q.popleft()
        if current == end:
            break
        for i in range(4):
            r = current[0] + dr[i]
            c = current[1] + dc[i]
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue
            if visited[r][c]:
                continue
            if binary[r][c] == 255:
                visited[r][c] = True
                parent[r][c] = current
                q.append((r, c))
    if not visited[end[0]][end[1]]:
        print("No path found")
        return None
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current[0]][current[1]]
    path.append(start)
    path.reverse()
    print("Path found!")
    print("Steps:", len(path))
    return path
def resize(image):
    h, w = image.shape[:2]
    if w > 600 or h > 600:
        scale = min(600 / w, 600 / h)
        w = int(w * scale)
        h = int(h * scale)
        image = cv2.resize(image, (w, h))
    return image
def show_path(image, path):
    result = image.copy()
    for i in range(1, len(path)):
        p1 = path[i - 1]
        p2 = path[i]
        cv2.line(
            result,
            (p1[1], p1[0]),
            (p2[1], p2[0]),
            (0, 255, 0),
            3
        )
        cv2.imshow("Maze Solution", resize(result))
        cv2.waitKey(1)
    start = path[0]
    cv2.circle(
        result,
        (start[1], start[0]),
        8,
        (255, 0, 0),
        -1
    )
    end = path[-1]
    cv2.circle(
        result,
        (end[1], end[0]),
        8,
        (0, 0, 255),
        -1
    )
    return result
def main():
    image = get_image()
    if image is None:
        print("Image not found!")
        return
    print("Image loaded")
    gray_image = gray(image)
    binary_image = black_white(gray_image)
    count_pixels(binary_image)
    maze_boundary(image, binary_image)
    start, end = find_points(image, binary_image)
    if start is None or end is None:
        print("Please give a maze with blue start and red end.")
        return
    path = solve(binary_image, start, end)
    if path is None:
        return
    result = show_path(image, path)
    cv2.imshow("Final Maze", resize(result))
    print("Press any key to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()