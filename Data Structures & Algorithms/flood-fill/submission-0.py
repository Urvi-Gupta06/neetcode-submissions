class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        if image[sr][sc]==color:
            return image

        def bfs(r,c):
            q = deque()
            visited = set()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            q.append((r,c))
            visited.add((r,c))

            while q:
                r,c = q.popleft()

                for dr,dc in directions:
                    if (dr+r in range(rows) and dc+c in range(cols) and (dr+r,dc+c) not in visited and image[r][c]==image[dr+r][dc+c]):
                        q.append((dr+r,dc+c))
                        visited.add((dr+r,dc+c))

                image[r][c]=color

            return image 
        return bfs(sr,sc)
