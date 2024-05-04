# Change these for different letters if you want. It's already configured for toki pona
consonants = ['m', 'n', 'p', 't', 'k', 's', 'w', 'l', 'j', '']
vowels = ['a', 'e', 'i', 'o', 'u']
coda = ['n', '']
forbidden_sequences = ['wu', 'wo', 'ji', 'ti', 'wan', 'won', 'jin', 'tin']

# DON'T TOUCH THESE I'M GONNA CRY (also the code is not going to work unless you modify all instances of 'starts' and 'syllables')
starts = []
syllables = []

# This checks for forbidden sequences 
def is_forbidden(s):
    for seq in forbidden_sequences:
        if seq in s:
            return True
    return False

# This generates the starting syllables, see README.md for info on phonotactics
def generate_start():
    for v in vowels:
        for c in consonants:
            for n in coda:
                if c == '' and n == '':
                    starts.append(v)
                elif c == '':
                    s = v + n
                    if not is_forbidden(s):
                        starts.append(s)
                elif n == '':
                    s = c + v
                    if not is_forbidden(s):
                        starts.append(s)
                else:
                    s = c + v + n
                    if not is_forbidden(s):
                        starts.append(s)
    return starts

# This generated syllables that are not at the start of a word, see README.md for info on phonotactics
def generate_syllables():
    for c in consonants:
        for v in vowels:
            for n in coda:
                if c != '' and n != '':
                    s = c + v + n
                    if not is_forbidden(s):
                        syllables.append(s)
                elif c != '':
                    s = c + v
                    if not is_forbidden(s):
                        syllables.append(s)
    return syllables

# This is so very very unnecessary but I do not care in the slightest fight me. It's a function that calls 2 other functions
def generate():
    generate_start()
    generate_syllables()

# Again, fight me
generate()

# This is the output you'll see in the console. I made it so that it preformats them into arrays for python and varName.sort() is to sort the output of each
print("start = ", end="")
starts.sort()
print(starts)
print("\nother = ", end="")
syllables.sort()
print(syllables)
# 69