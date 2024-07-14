# How would you handle parsing a log file and extracting specific information?

def find_in_log(file, string):
	found = False
	with open(file, "r") as f1:
		for line in f1:
			if string in line:
				print(line.strip("\n"))
				found = True
	return found

print(find_in_log("log.txt", "error"))  # False
print(find_in_log("log.txt", "Success"))  # True
print(find_in_log("log.txt", "IOError"))  # True

