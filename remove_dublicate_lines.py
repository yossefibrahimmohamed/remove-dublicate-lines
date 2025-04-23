def remove_duplicates(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    unique_lines = list(dict.fromkeys(lines))

    with open(file_path, "w") as f:
        f.writelines(unique_lines)

    print("✅ Duplicate lines removed successfully.")


remove_duplicates("subdomians.txt")
