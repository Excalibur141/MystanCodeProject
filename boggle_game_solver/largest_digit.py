"""
File: largest_digit.py
Name: Jhin
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	# Only compare positive integers
	if n < 0:
		n = n * -1

	# Base case
	if n < 10:
		return n
	elif n == 9:
		return n
	# Self-similarity
	else:
		# Units digit
		n10 = n % 10
		# Tens digit
		n100 = (n % 100 - n % 10) // 10
		# under the assumption that for loop cannot be used
		# only division can be used to determine the size of units and tens digits
		if n10 > n100:  # units digit > tens digit
			return find_largest_digit((n - n % 100) / 10 + n % 10)
		if n10 <= n100:  # units digit <= tens digit
			return find_largest_digit(n // 10)


if __name__ == '__main__':
	main()
