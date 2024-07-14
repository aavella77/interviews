# 57. Insert Interval
# Medium
# Topics
# Companies
# Hint
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# Note that you don't need to modify intervals in-place. You can make a new array and return it.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
# Constraints:
#
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105

def binary_search(list, target):
	left = 0
	right = len(list) - 1

	while left <= right:
		mid = (left + right) // 2
		if target == list[mid]:
			return mid
		elif target > list[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return -1

def insert_interval(intervals, new_interval):
	output = []
	i, n = 0, len(intervals)

	# Iterate over the intervals.
	# If the current interval ends before the new interval starts, add the current interval to the output.
	while i < n and intervals[i][1] < new_interval[0]:
		output.append(intervals[i])
		i += 1

	# If the current interval overlaps with the new interval, merge them by updating the start and end of the new interval.
	merge_start, merge_end = new_interval[0], new_interval[1]
	#
	# intervals[i][0] <= new_interval[1]: This part of the condition is checking if the start of the current interval (intervals[i][0]) is less than or equal to the end of the new_interval. This is used to determine if the current interval overlaps with the new_interval.
	while i < n and intervals[i][0] <= new_interval[1]:
		print("merge start check: ", intervals[i][0], new_interval[0])
		merge_start = min(intervals[i][0], merge_start)
		merge_end = max(intervals[i][1], merge_end)
		print("current merge ", merge_start, merge_end)
		i += 1

	# Append merged interval
	if merge_start is not None and merge_end is not None:
		output.append([merge_start, merge_end])

	# Add all the rest
	while i < n:
		output.append(intervals[i])
		i += 1

	return output




# Copilot says that binary search is not needed
def insert_interval_binary_search(intervals, new_interval):
	output = []
	intervals_flat = []
	for interval in intervals:
		for idx in range(interval[0], interval[1] + 1):
			intervals_flat.append(idx)
	print(intervals_flat)
	start = new_interval[0]
	end = new_interval[1]
	start_pos = binary_search(intervals_flat, start)
	end_pos = binary_search(intervals_flat, end)
	print(f"start {start} start_pos {start_pos}, end {end} end_pos {end_pos}")
	for interval in intervals:
		if interval[1] < start:
			output.append(interval)
		elif interval[0] > end:
			output.append([start, end])
			output.append(interval)
		else:
			start = min(start, interval[0])
			end = max(end, interval[1])
	return output

print(insert_interval( [[1,3], [6,9]], [2, 5]), end="\n\n")  # [[1,5], [6,9]]
print(insert_interval( [[1,2],[3,5],[6,7],[8,10],[12,16], [17, 18], [23,25]], [4,8] )) # [[1,2], [3, 10], [12, 16], [17, 18], [23, 25]]