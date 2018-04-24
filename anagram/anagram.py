def detect_anagrams(word, candidates):
    same = []
    letters = []

    for letter in word:
        letters.append(letter.lower())

    for candidate in candidates:
        candidate_letters = []

        for letter in candidate:
            candidate_letters.append(letter.lower())
        
        if (sorted(letters) == sorted(candidate_letters) and not
            letters == candidate_letters):
            same.append(candidate)

    return same    

candidates = ["hello", "world", "zombies", "pants"]
detect_anagrams("diaper", candidates)
