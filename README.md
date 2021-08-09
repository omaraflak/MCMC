# Markov Chain Monte Carlo

Simple application of the Markov Chain Monte Carlo (MCMC) method to decrypt a text that was encrypted by letters substitutions.

```python
from preprocessing import FrequencyTable
from mcmc import encrypt, decrypt, random_mapping

# build a frequency table using "book.txt"
# the frequency table contains the number of occurences of 2 successive letters
# example: {"TH": 230, "AR": 102, ...}
table = FrequencyTable.from_file("book.txt")

# build a random mapping
# example: {"a": "c", "b": "z", ...}
mapping = random_mapping(list(table.letters))

# random plain text that is going to be encrypted then decrypted
text = "The world is changing faster than ever. Breakthroughs in areas from artificial intelligence to biotechnologies are now permeating our daily lives at a relentless pace. Advances in engineering and technology are creating opportunities to transform the way things are made and to address global challenges and sustainable development goals."

# encrypt the plain text using the randomly generated mapping
secret = encrypt(mapping, text)

# recover the inverse mapping using the frequency table
inverse_mapping = decrypt(table, secret)
```