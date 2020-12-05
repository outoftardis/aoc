import hashlib
secret_key = "iwrupvqb"


def generate_md5(key):
    m = hashlib.md5()
    m.update(key.encode("utf-8"))
    return m.hexdigest()


def check(md5sum, n):
    return md5sum[:n] != "0" * n


def create_key(key, i):
    return key + str(i)


# part 1, 2

not_found = True
i = 0
while not_found:
    i += 1
    new_key = create_key(secret_key, i)
    md5sum = generate_md5(new_key)
    not_found = check(md5sum, 6)  # check(md5sum, 6)


print(i)