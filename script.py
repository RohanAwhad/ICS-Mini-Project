#!/usr/bin/env python3

import random

def one_time_pad(length):
	chars = [chr(i) for i in range(ord('a'), ord('z')+1)]
	chars.remove('j')
	ret = ''
	for i in range(length): ret = ret + random.choice(chars)
	return ret

def create_matrix(keyword):
	matrix = []
	char_complete = set()
	keyword_index = 0
	alphabet_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
	alphabet_list.remove('j')
	alphabet_index = 0
	i, j = 0, 0
	while (i < 5):
		j = 0
		temp = []
		while (j < 5):
			if keyword_index < len(keyword):
				letter = keyword[keyword_index]
				keyword_index += 1
			else:
				letter = alphabet_list[alphabet_index]
				alphabet_index += 1
			if letter in char_complete:
				continue
			else:
				temp.append(letter)
				char_complete.add(letter)
			j += 1
		matrix.append(temp)
		i += 1

	return matrix

def rail_transformation(text):
	flag = True
	upper = ''
	lower = ''
	for i in text:
		if flag: upper = upper + i
		else: lower = lower + i
		flag = not flag

	return upper + lower

def get_pairs(plaintext):
	# Get pairs
	pairs = []
	i = 0
	while (i < len(plaintext)):
		if (i+1) == len(plaintext): 
			pairs.append((plaintext[i], 'x'))
		elif plaintext[i] != plaintext[i+1]: 
			pairs.append((plaintext[i], plaintext[i+1]))
		else:
			pairs.append((plaintext[i], 'x'))
			i -= 1
		i += 2

	return pairs

def get_position(pair, matrix):
	a, b = pair
	for j in range(5):
		if a in matrix[j]:
			a_pos = (j, matrix[j].index(a))
		if b in matrix[j]:
			b_pos = (j, matrix[j].index(b))

	return (a_pos, b_pos)
		
def encrypt(pos, matirx):
	ciphertext = []
	# same row
	if pos[0][0] == pos[1][0]:
		ciphertext.append((matrix[pos[0][0]][(pos[0][1] + 1) % 5], matrix[pos[1][0]][(pos[1][1] + 1) % 5]))

	# same col
	elif pos[0][1] == pos[1][1]:
		ciphertext.append((matrix[(pos[0][0]+1) % 5][pos[0][1]], matrix[(pos[1][0]+1) % 5][pos[1][1]]))

	# neither
	else:
		ciphertext.append((matrix[pos[0][0]][pos[1][1]], matrix[pos[1][0]][pos[0][1]]))

	ciphertext = ''.join(i+j for (i,j) in ciphertext)
	return ciphertext

def decrypt(pos, matrix):
	plaintext = []
	# same row
	if pos[0][0] == pos[1][0]:
		plaintext.append((matrix[pos[0][0]][pos[0][1] - 1], matrix[pos[1][0]][pos[1][1] - 1]))

	# same col
	elif pos[0][1] == pos[1][1]:
		plaintext.append((matrix[pos[0][0] - 1][pos[0][1]], matrix[pos[1][0] - 1][pos[1][1]]))

	# neither
	else:
		plaintext.append((matrix[pos[0][0]][pos[1][1]], matrix[pos[1][0]][pos[0][1]]))

	plaintext = ''.join(i+j for (i,j) in plaintext)
	return plaintext


if __name__ == '__main__':
	message = ''.join(i for i in input('Enter message: ').lower().split(' '))
	print("Original Message: ", message)

	keyword = one_time_pad(len(message))
	pairs = get_pairs(message)
	key = keyword
	ciphertext = ''
	for pair in pairs:
		matrix = create_matrix(key)
		pos = get_position(pair, matrix)
		ciphertext += encrypt(pos, matrix)
		key = rail_transformation(key)

	print('Encrypted Message: ', ciphertext)

	pairs = get_pairs(ciphertext)
	key = keyword
	plaintext = ''
	for pair in pairs:
		matrix = create_matrix(key)
		pos = get_position(pair, matrix)
		plaintext += decrypt(pos, matrix)
		key = rail_transformation(key)

	print('Decrypted Message: ', plaintext)

	print('Is original message equal to decrypted message? ', message==plaintext)

