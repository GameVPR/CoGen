import os

# Set the console window title to "RASDA"
os.system("title CoGen Anti-Duper V0.1")

# Size of each chunk to read from the file
CHUNK_SIZE = 1000000

# Set to store all codes seen so far
seen_codes = set()

# Function to check for duplicate codes within a chunk
def check_duplicates(codes):
    duplicates = set()
    for code in codes:
        if code in seen_codes:
            duplicates.add(code)
        else:
            seen_codes.add(code)
    return duplicates

# Read the file in chunks and check for duplicates within each chunk
with open('codes.txt', 'r') as f:
    chunk = f.readlines(CHUNK_SIZE)
    while chunk:
        # Split the chunk into individual codes
        codes = [code.strip() for code in chunk]
        # Check for duplicates within the chunk
        duplicates = check_duplicates(codes)
        # Remove duplicates from the chunk
        codes = list(set(codes) - duplicates)
        # Append the remaining codes to the temporary output file
        with open('fix.tmp', 'a') as out:
            out.write('\n'.join(codes) + '\n')
        # Read the next chunk
        chunk = f.readlines(CHUNK_SIZE)

# Close the input file
f.close()

# Delete the original file
os.remove('codes.txt')

# Rename the temporary output file to codes.txt
os.rename('fix.tmp', 'codes.txt')

# Print a message indicating that the process is complete
print('Done')

# Wait for user to close tab
input("Press Enter to close the program...")
