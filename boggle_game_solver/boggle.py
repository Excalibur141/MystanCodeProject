"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	1. Save list
		1-1 case-insensitive
		1-2 raw = l1, l2, l3 ,l4 (i)
		1-3 column = 0, 1, 2, 3 (j)
		1-4 list = [[l1], [l2], [l3], [l4]]
	2. Organize dictionary
		2-1 delete len(word) < 3
		2-2 delete word without input ch
	3. Search word
		3-1 build a word by
	"""
	start = time.time()
	####################
	# 1. Save list
	boggle_list = []
	count = 1
	while True:
		if count == 5:
			break
		row = input(str(count)+' row of letters: ').lower()
		if len(row) != 8:
			print("Illegal input")
		else:
			short = []
			for word in row:
				if word.isalpha():
					short.append(word)
			boggle_list.append(short)
			count += 1
	# print(boggle_list)  # only for test
	# 2. Organize dictionary
	dictionary_list = read_dictionary(boggle_list)
	# add filter
	check_list = []
	double_list = []
	for i in range(len(boggle_list)):
		for j in range(len(boggle_list)):
			if boggle_list[i][j] not in check_list:
				check_list.append(boggle_list[i][j])
			else:
				double_list.append(boggle_list[i][j])
	# print(double_list)  # only for test
	# 3. Search word
	ans_list = []
	for i in range(len(boggle_list)):
		for j in range(len(boggle_list)):
			find_word(boggle_list, dictionary_list, boggle_list[i][j], ans_list, i, j, double_list)
	print("There are", len(ans_list), "words in total.")
	"""
	# f y c l #
	# i o m g #
	# o r i l #
	# h j h u #
	"""
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(boggle_list, dictionary_list, current_s, ans_list, i, j, check_list):
	if len(current_s) == 4:
		if current_s in dictionary_list:
			if current_s not in ans_list:
				print("Found:", current_s)
				ans_list.append(current_s)
	else:
		# select surrounding ch
		for x in range(-1, 2, 1):
			for y in range(-1, 2, 1):
				if 0 <= x + i < len(boggle_list):
					if 0 <= y + j < len(boggle_list):
						if x != 0 or y != 0:  # don't choose yourself
							# don't look back
							if boggle_list[x + i][y + j] not in current_s or boggle_list[x + i][y + j] in check_list:
								# print("(i,j):", (i, j), "|", "(x,y):", (x, y), "|", "(x+i,y+j):", (x + i, y + j))  # only for test
								# Choose
								current_s += boggle_list[x + i][y + j]
								# print("current_s:", current_s)  # only for test
								# Explore
								new_x = x + i
								new_y = y + j
								if has_prefix(current_s, dictionary_list):
									find_word(boggle_list, dictionary_list, current_s, ans_list, new_x, new_y, check_list)
								# Un-choose
								current_s = current_s[:-1]


def read_dictionary(boggle_list):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	# ch filter
	all_ch_list = []
	for i in range(len(boggle_list)):
		for j in range(len(boggle_list)):
			if boggle_list[i][j] not in all_ch_list:
				all_ch_list.append(boggle_list[i][j])
	# print(all_ch_list)  # only for test

	dictionary_list = []
	count = 0
	with open(FILE, 'r') as f:
		for line in f:
			dictionary = line.strip()
			# filter by ch length
			if len(dictionary) == 4 or len(dictionary) == 5:
				# filter by ch that occur
				for ch in all_ch_list:
					if dictionary.startswith(ch):
						count += 1
						dictionary_list.append(dictionary)
	# print(count)  # only for test
	return dictionary_list


def has_prefix(sub_s, dictionary_list):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary_list: list
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
