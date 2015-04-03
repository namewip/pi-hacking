import sys

sample_file = open(sys.argv[1])
calced_file = open(sys.argv[2])

good_digits = 0

while True:
    sample = sample_file.read(1)
    calced = calced_file.read(1)
    if not sample:
    	sys.exit(1)
    if (not calced) or (sample != calced):
        break
    else:
        good_digits += 1

print(str(good_digits - 2))
