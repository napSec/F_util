# created by napSec for use by anyone. Please star and share this repo if it was helpful

import sys
import os

def compare_files(file1, file2):
    result = "Files are different"
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        if f1.read() == f2.read():
            result = "Files are the same"
    return result

def search_file(filename, word):
    result = f"{word} not found in {filename}"
    with open(filename, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if word in line:
                result = f"{word} found in line {i+1} of {filename}"
                break
    return result

def decode_file(filename, encoding):
    result = ""
    with open(filename, "r", encoding=encoding) as f:
        result = f.read()
    return result

def encode_file(filename, encoding):
    with open(filename, "r") as f:
        content = f.read()
    with open(filename, "w", encoding=encoding) as f:
        f.write(content)

def unzip_file(filename):
    os.system(f"unzip {filename}")

def extract_exif(filename):
    result = os.popen(f"exiftool {filename}").read()
    return result

def extract_metadata(filename):
    result = os.popen(f"exiv2 {filename}").read()
    return result

def search_urls(filename):
    result = ""
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "http://" in line or "https://" in line:
                result += line
    return result

def main():
    while True:
        print("1. Compare Files")
        print("2. Search File")
        print("3. Decode File")
        print("4. Encode File")
        print("5. Unzip File")
        print("6. Extract EXIF")
        print("7. Extract Metadata")
        print("8. Search URLs")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")
        if choice == "1":
            file1 = input("Enter the first file name: ")
            file2 = input("Enter the second file name: ")
            result = compare_files(file1, file2)
            print(result)
        elif choice == "2":
            filename = input("Enter the file name: ")
            word = input("Enter the word to search for: ")
            result = search_file(filename, word)
            print(result)
        elif choice == "3":
            filename = input("Enter the file name: ")
            encoding = input("Enter the encoding to use (e.g. UTF-8): ")
            result = decode_file(filename, encoding)
            print(result)
        elif choice == "4":
            filename = input("Enter the file name: ")
            encoding = input("Enter the encoding to use (e.g. UTF-8): ")
            encode_file(filename, encoding)
            print(f"File {filename} encoded with {encoding}")
        elif choice == "5":
            filename = input("Enter the file name: ")
            unzip_file(filename)
            print(f"File {filename} unzipped")
        elif choice == "6":
            filename = input("Enter the file name: ")
            result = extract_exif(filename)
            print(result)
        elif choice == "7":
            filename = input("Enter the file name: ")
            result = extract_metadata(filename)
            print(result)
        elif choice == "8":
            filename = input("Enter the file name: ")
            result = search_urls(filename)
            print(result)
        elif choice == "9":
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
