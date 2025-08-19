import hashlib

def calculate_hash(file_path, algorithm="sha256"):
    """
    Calculate hash of a file.
    Supported algorithms: md5, sha1, sha256
    """
    hash_func = getattr(hashlib, algorithm)()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
        return None

def main():
    print("=== File Integrity Checker ===")
    file_path = input("Enter the file path to check: ")
    algorithm = input("Enter hash algorithm (md5/sha1/sha256) [sha256]: ") or "sha256"

    original_hash = input("Enter original hash (leave blank to generate new hash): ")

    current_hash = calculate_hash(file_path, algorithm)
    if current_hash is None:
        return

    print(f"[+] Current {algorithm.upper()} hash: {current_hash}")

    if not original_hash:
        print("[*] Save this hash for future integrity checks.")
    else:
        if current_hash == original_hash:
            print("[✔] File is intact. No modifications detected.")
        else:
            print("[✖] File has been modified!")

if __name__ == "__main__":
    main()
