import heapq

def kClosest(points, k):
    def distance(point):
        return point[0] ** 2 + point[1] ** 2

    heap = []

    for point in points:
        dist = -distance(point)
        if len(heap) < k:
            heapq.heappush(heap, (dist, point))
        else:
            if dist > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (dist, point))

    return [point for (dist, point) in heap]


points1 = [[1, 3], [-2, 2]]
k1 = 1
print(kClosest(points1, k1))

points2 = [[3, 3], [5, -1], [-2, 4]]
k2 = 2
print(kClosest(points2, k2))