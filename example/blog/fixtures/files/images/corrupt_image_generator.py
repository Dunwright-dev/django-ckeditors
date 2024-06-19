"""Generate corrupted image files for testing"""

import os
import random


def corrupt_image(filename, corruption_level=0.1):
    """Corrupts a percentage of bytes in the image file and saves it with
    '_corrupted' suffix, leaving the original intact.
    """
    # Open original in read binary mode
    with open(filename, "rb") as original_file:
        image_data = original_file.read()  # Read all data into memory

    corrupted_data = bytearray(image_data)  # Create a copy for corruption

    # Corrupt the data (same logic as before)
    for _ in range(int(len(image_data) * corruption_level)):
        position = random.randint(0, len(image_data) - 1)
        corrupted_data[position] = random.randint(0, 255)

    # Save the corrupted file
    base_filename, extension = os.path.splitext(filename)
    new_filename = base_filename + "_corrupted" + extension
    with open(new_filename, "wb") as corrupted_file:
        corrupted_file.write(corrupted_data)  # Write corrupted data to new file


if __name__ == "__main__":
    # Example usage:
    corrupt_image("test.png")
