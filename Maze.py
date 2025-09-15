from collections import deque
class Solution(object):
    def maze(self, grid, start, end):
        visited = set()
        queue = deque([start])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        while queue:
            x, y = queue.popleft()
            if(x,y) == end:
                return True

            visited.add((x,y))

            for dx, dy in directions:
                nx, ny = dx+x, dy+y

                if (nx >= 0 and nx < len(grid) and ny >= 0 and
                    ny < len(grid[0]) and (nx,ny) not in visited
                    and grid[nx][ny] == 0):
                    queue.append((nx,ny))
        return False


def main():
    sol = Solution()
    maze = [
            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0],
            [1, 1, 1, 0]
           ]
    start = (0, 0)
    destination = (3, 3)
    result = sol.maze(maze, start, destination)
    print(result)

if __name__ == "__main__":
    main()
