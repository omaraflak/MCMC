from preprocessing import FrequencyTable
from mcmc import encrypt, decrypt, random_mapping

def main():
    table = FrequencyTable.from_file("book.txt")
    mapping = random_mapping(list(table.letters))
    text = "The world is changing faster than ever. Breakthroughs in areas from artificial intelligence to biotechnologies are now permeating our daily lives at a relentless pace. Advances in engineering and technology are creating opportunities to transform the way things are made and to address global challenges and sustainable development goals."
    secret = encrypt(mapping, text)
    inverse_mapping = decrypt(table, secret)

if __name__ == "__main__":
    main()