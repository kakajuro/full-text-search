from util.findNth import find_nth

def fullTextSearch(target, arr, mode):

	if mode == "c" or mode == "w" or mode == "i" or mode == "wi":
		pass
	else:
		raise Exception("Invalid mode.")

	foundIndexes = []
	foundWords = []
	foundCount = 0
		
	for word in arr:

		if len(word) < len(target):
			pass
		else:

			brokenWord = list(word)
			seen = []

			for x in range(len(word)):
				if len(word) == len(target):
					if word == target and word not in foundWords:
						foundCount+=1
						foundWords.append(word)
				elif len(word) > len(target):
					for char in brokenWord:
						try:

							if seen.count(char) > 1:

								result = [item for item in seen if item == char]
								count = len(result)

								for x in range(count):

									indexOfRepeat = find_nth(word, char, x)
									nextChar = indexOfRepeat + 1

									currentString = brokenWord[indexOfRepeat] + brokenWord[nextChar]

									if currentString == target and word not in foundWords:
										foundCount+=1
										foundWords.append(word)

									seen.append(char)

							else:
								nextChar = brokenWord.index(char) + 1
								currentString = char + brokenWord[nextChar]

								if currentString == target and word not in foundWords:
									foundCount+=1
									foundWords.append(word)

								seen.append(char)


						except IndexError:
							lastChar = brokenWord.index(char) - 1
							currentString = brokenWord[lastChar] + char

							if currentString == target and word not in foundWords:
								foundCount+=1
								foundWords.append(word)

							seen.append(char)

						#finally:
							# Debug: print(f"char: {char}, currentString: {currentString}")

	if foundWords:

		indexes = []

		for word in foundWords:
			indexes.append(arr.index(word))

	if mode == "c":
		return foundCount
	elif mode == "w":
		return foundWords
	elif mode == "i":
		
		if indexes:
			return indexes
		else:
			return "No matches found."

	elif mode == "wi":
		
		if foundWords:
			if indexes:
				return foundWords, indexes
			else:
				return foundWords
		else:
			return "No matches found."

	print(f"foundCount: {foundCount}, foundWords: {foundWords}")

# Example 
# print(fullTextSearch('hi', ['hello', 'hi', 'hi there', 'hills', 'bonjour', 'a'], "wi"))
