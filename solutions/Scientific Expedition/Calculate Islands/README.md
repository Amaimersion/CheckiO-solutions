The Robots have found a chain of islands in the middle of the Ocean. They would like to explore these islands and have asked for your help calculating the areas of each island. They have given you a map of the territory. The map is a 2D array, where 0 is water, 1 is land. An island is a group of land cells surround by water. Cells are connected by their edges and corners. You should calculate the areas for each of the islands and return a list of sizes (quantity of cells) in ascending order. All of the cells outside the map are considered to be water.

Input: A map as a list of lists with 1 or 0.
Output: The sizes of island as a list of integers.

Precondition: 0 < len(land_map) < 10
all(len(land_map[0]) == len(row) for row in land_map)
any(any(row) for row in land_map)