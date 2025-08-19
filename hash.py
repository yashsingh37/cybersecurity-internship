import hashlib

def generate_hashes(file_path):
    # Define hash algorithms
    hash_md5 = hashlib.md5()
    hash_sha1 = hashlib.sha1()
    hash_sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:
            # Read file in chunks (good for large files)
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
                hash_sha1.update(chunk)
                hash_sha256.update(chunk)

        print(f"File: {file_path}")
        print(f"MD5:    {hash_md5.hexdigest()}")
        print(f"SHA1:   {hash_sha1.hexdigest()}")
        print(f"SHA256: {hash_sha256.hexdigest()}")

    except FileNotFoundError:
        print("❌ File not found!")

# Example usage
file_name = "test.txt"
generate_hashes(file_name)
