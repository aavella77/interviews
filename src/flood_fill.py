# 733. Flood Fill
# Easy
# Topics
# Companies
# Hint
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
#
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
#
# Return the modified image after performing the flood fill.
#
#
#
# Example 1:
#
#
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
# Example 2:
#
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made to the image.
#
#
# Constraints:
#
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 216
# 0 <= sr < m
# 0 <= sc < n

class Solution:
	def floodFill(self, image, sr: int, sc: int, color: int):
		originalColor = image[sr][sc]
		if originalColor == color:
			return image

		def dfs(x: int, y: int):
			if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != originalColor:
				return
			image[x][y] = color
			directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
			for dx, dy in directions:
				dfs(x + dx, y + dy)

		dfs(sr, sc)
		return image

# If the colors are the same, return image is executed. This means the function will end and return the original image without making any changes because there's no need to perform a flood fill operation if the starting pixel is already of the color that you want to fill.

# At the end of the floodFill function, after the dfs function has been called. Here, it returns the modified image after the flood fill operation has been performed. The dfs function modifies the image in-place, meaning it directly changes the original image array. Therefore, when return image is executed, it returns the image with the updated colors.
# In Python, lists (which are being used to represent the image) are mutable objects, so any changes made to them inside a function will affect the original list. That's why the changes made by the dfs function persist in the image even after the function has finished executing.

# The recursion is implemented through a helper function called dfs (short for Depth-First Search). Here's how it works:
# The dfs function is called with the coordinates of the starting pixel.
# Inside the dfs function, it first checks if the current pixel is within the image boundaries and if its color is the same as the original color of the starting pixel. If either condition is not met, the function returns without making any further recursive calls. This is the base case of the recursion.
# If the base case conditions are met, it changes the color of the current pixel to the new color.
# Then, it calls itself for each of the 4-directionally connected pixels. This is the recursive step. The recursion continues until all the pixels that are connected to the starting pixel and have the same color as the original color of the starting pixel have been visited and their color changed.
# The recursion starts when the dfs function is first called in the floodFill function with the starting pixel coordinates.
# In this way, the dfs function recursively explores the image, changing the color of all the pixels that are connected to the starting pixel and have the same color as the original color of the starting pixel.

# Time Complexity: The time complexity of the flood fill algorithm is O(m*n), where m is the number of rows and n is the number of columns in the image. This is because in the worst-case scenario, the algorithm might have to visit all the pixels in the image once.
#
# Space Complexity: The space complexity of the flood fill algorithm is O(m*n), where m is the number of rows and n is the number of columns in the image. This is due to the potential maximum depth of the recursive call stack. In the worst-case scenario, the depth of the recursion could be as large as the number of pixels in the image, which happens when all the pixels in the image have the same color.

my_solution = Solution()
print(my_solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
print(my_solution.floodFill([[0,0,0],[0,0,0]], 0, 0, 0))
print(my_solution.floodFill([[0,0,0],[0,1,1]], 1, 1, 1))
print(my_solution.floodFill([[0,0,0],[0,1,1]], 1, 1, 2))
