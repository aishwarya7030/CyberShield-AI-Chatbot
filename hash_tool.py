import hashlib


def generate_hash(text):
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()

    return {
        "MD5": md5_hash,
        "SHA1": sha1_hash,
        "SHA256": sha256_hash
    }
