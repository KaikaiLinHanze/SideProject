"""
File: boggle.py
Name: Kai
----------------------------------------
find all the anagram in the boggle.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dic = {}
count = 0


def main():
	"""
	find all the anagram in the boggle.
	"""
	read_dictionary()
	data = in_put_data()
	ans = []
	cur = []
	for i in range(4):
		for j in range(4):
			cur.append([i, j])
			find_anagrams(i, j, data, cur, ans)
			cur.pop()
	print(f'There are {len(ans)} words in the boggle.')


def in_put_data():
	"""
	:return input data
	"""
	words = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
	return words


def find_anagrams(x, y, in_put_list, cur, answer):
	"""
	:param x: x index for the input digit
	:param y: y index for the input digit
	:param in_put_list: list, the entered listed of boggle
	:param cur: list, the temporary list for boggle calculation
	:param answer: list, the final list of boggle found
	"""
	# Base case
	if len(cur) >= 4:
		word = ''
		for site in cur:
			x_site = site[0]
			y_site = site[1]
			word += in_put_list[x_site][y_site]
		if word in dic and word not in answer:
			answer.append(word)
			print('Found: ' + word)
	if len(cur) < 5:
		# Explore
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i == 0 and j == 0:
					pass
				else:
					if 0 <= x + i <= 3 and 0 <= y + j <= 3:
						if [x+i, y+j] not in cur:
							cur.append([x+i, y+j])
							find_anagrams(x+i, y+j, in_put_list, cur, answer)
		# Un-choose
							cur.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dic
	with open(FILE, mode="r") as f:
		for line in f:
			dic[line.strip()] = 0


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for ch in dic:
		if ch.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
