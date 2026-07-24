import filetype
import os


def detect_file(path):
    if not os.path.exists(path):
        print("❌ File not found!")
        return

    kind = filetype.guess(path)

    if kind is None:
        print("\n⚠️ Unknown file type.")
    else:
        print("\n📄 File Information")
        print("-" * 30)
        print(f"Extension : {kind.extension}")
        print(f"MIME Type : {kind.mime}")


def main():
    print("=" * 40)
    print("      FILE TYPE DETECTOR")
    print("=" * 40)

    file_path = input("\nEnter file path: ").strip()

    detect_file(file_path)


if __name__ == "__main__":
    main()