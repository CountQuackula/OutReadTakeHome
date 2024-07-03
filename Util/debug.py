import sys

def showAbstracts(data_from_folder) -> None:
    print("Data from Folder:")
    num = 0
    for title, abstract in data_from_folder:
        # Check if abstract is not empty or None
        if abstract and abstract.strip():  # Check if abstract is not empty or only whitespace
            num += 1
            print(f"Title: {title}")
            print(f"Abstract: {abstract}\n")
        else:
            sys.exit("Empty abstract found. Stopping further printing.")
    print(f"Total entries: {num}")

def showPreprocessed(preprocessed_data):
    print("Preprocessed data:")
    print(preprocessed_data)

def showVectorized(vec: list[list[float]]) -> None:
    print("Vectorized data:")
    print(vec)

