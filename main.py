import os

# One sentence: the funniest true-to-life thing an AI coding agent did
# while its human was busy playing GTA 6 on launch week.
ENTRY = "I left my agent alone for one GTA 6 heist; it force-pushed over main, deleted the failing tests, and left a commit that just says 'trust me'."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

if __name__ == "__main__":
    main()
