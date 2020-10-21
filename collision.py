import hashlib

''' Function opens the wordlist, hashes all entries, selects the first 6
    characters of the hashed value and writes the outputs to two new files'''

def collision():
    file = open("word_list.txt", "r", encoding="latin1")
    f1 = file.read()
    f2 = f1.split("\n")
    file.close()

    entry_list = []

    hashes = open("hashes1.txt", "w")
    value_and_hash = open("hashes2.txt","w")

    for i in f2:
        hash_obj = hashlib.sha1((bytes(i, encoding = "utf-8"))).hexdigest()
        entry_list.append(str(hash_obj))
        hashes.write(str(hash_obj)[:6] +  "\n")
        value_and_hash.write(i +"-" + str(hash_obj)[:6] +  "\n")
    hashes.close()
    value_and_hash.close()
    

    print("\nHashing finished")

collision()