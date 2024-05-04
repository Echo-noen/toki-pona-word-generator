import itertools
from tqdm import tqdm

# These come from syllables.py. Is there a better way? Probably, but idk python
start = ['a', 'an', 'e', 'en', 'i', 'in', 'ja', 'jan', 'je', 'jen', 'jo', 'jon', 'ju', 'jun', 'ka', 'kan', 'ke', 'ken', 'ki', 'kin', 'ko', 'kon', 'ku', 'kun', 'la', 'lan', 'le', 'len', 'li', 'lin', 'lo', 'lon', 'lu', 'lun', 'ma', 'man', 'me', 'men', 'mi', 'min', 'mo', 'mon', 'mu', 'mun', 'na', 'nan', 'ne', 'nen', 'ni', 'nin', 'no', 'non', 'nu', 'nun', 'o', 'on', 'pa', 'pan', 'pe', 'pen', 'pi', 'pin', 'po', 'pon', 'pu', 'pun', 'sa', 'san', 'se', 'sen', 'si', 'sin', 'so', 'son', 'su', 'sun', 'ta', 'tan', 'te', 'ten', 'to', 'ton', 'tu', 'tun', 'u', 'un', 'wa', 'we', 'wen', 'wi', 'win']
other = ['ja', 'jan', 'je', 'jen', 'jo', 'jon', 'ju', 'jun', 'ka', 'kan', 'ke', 'ken', 'ki', 'kin', 'ko', 'kon', 'ku', 'kun', 'la', 'lan', 'le', 'len', 'li', 'lin', 'lo', 'lon', 'lu', 'lun', 'ma', 'man', 'me', 'men', 'mi', 'min', 'mo', 'mon', 'mu', 'mun', 'na', 'nan', 'ne', 'nen', 'ni', 'nin', 'no', 'non', 'nu', 'nun', 'pa', 'pan', 'pe', 'pen', 'pi', 'pin', 'po', 'pon', 'pu', 'pun', 'sa', 'san', 'se', 'sen', 'si', 'sin', 'so', 'son', 'su', 'sun', 'ta', 'tan', 'te', 'ten', 'to', 'ton', 'tu', 'tun', 'wa', 'we', 'wen', 'wi', 'win']

# In case you need to configure your own syllables just modify the forbidden_substrings variable in generate_combinations()
def has_forbidden_substring(words, forbidden):
    for word in words:
        if any(substring in word for substring in forbidden):
            return True
    return False

def generate_combinations(start, other, num_terms):
    # Change this to change the file name
    filename = f"tp_{num_terms}_syllable_words.txt"
    # sina sona e ni come on
    forbidden_substrings = ['nn', 'nm']
    with open(filename, 'w') as file:
        # Here you calculate the total number of combinations possible, which is like only useful for the progress bar
        total_combinations = len(start) * len(other) ** (num_terms - 1)
        progress_bar = tqdm(total=total_combinations, desc="Writing combinations")

        for s in start:
            # other contains the list of all syllables that can exist in any position that is not the 1st, and itertools takes the number of terms inputted and generates all possible combinations of length num_terms - 1 (the first syllable is already there, in start - that's why the minus 1) with the elements of other
            other_combinations = itertools.product(other, repeat=num_terms - 1)
            # Loop through each of the other_combinations
            for o_combination in other_combinations:
                # Combine the start syllables with the other syllables (other_combinations)
                combination = [s] + list(o_combination)
                # If it doesn't have a forbidden substring,
                if not has_forbidden_substring(combination, forbidden_substrings):
                # Write the word to the file
                    file.write(''.join(combination) + '\n')
                # Update the progress bar
                progress_bar.update(1)
        
        # Close the progress bar
        progress_bar.close()

# Uuh input stuff or whatever
num_terms = int(input("Enter the number of terms for combinations: "))
generate_combinations(start, other, num_terms)
# And this is for when it's done
print(f"Combinations with {num_terms} terms have been generated and saved to tp_{num_terms}_syllable_words.txt")