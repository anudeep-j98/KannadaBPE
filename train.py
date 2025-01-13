import re
import string
from pathlib import Path
from tqdm import tqdm
from Byte_Pair_encoding import BytePairEncoding

import re
from utils import remove_emojis, clean_text


def load_text(directory: str) -> str:
    """
    Load and Preprocess Kannada text from files in directory
    
    Args:
        directory: Path to directory containing text files
        max_files: Maximum number of files to load (None for all files)
    """
    all_text = []
    
    # Convert to Path object for easier handling
    dir_path = Path(directory)
    
    # Get list of files and limit if specified
    files = list(dir_path.glob('*.txt'))
    
    # Process each file
    for file_path in tqdm(files, desc="Loading files"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                cleaned_text = clean_text(text)
                if cleaned_text:
                    all_text.append(cleaned_text)
        except UnicodeDecodeError:
            print(f"Warning: Skipping file {file_path} due to encoding issues")
    
    # Join all texts with space
    combined_text = ' '.join(all_text)
    
    print(f"Loaded {len(all_text):,} files")
    print(f"Total text length: {len(combined_text):,} characters")
    
    return combined_text

if __name__ == "__main__":
    data_dir = "data/"
    vocab_size = 3500
    output_file = "./encoding/kannada_tokenizer.json"
    
    text = load_text(data_dir)
    
    
    # train and save encoder
    print("\nTraining BPE encoder...")
    encoder = BytePairEncoding(text)
    encoder.encode_to_vocab_size(vocab_size, print_interval=100)
    
    # Save the encoder
    print("\nSaving encoder...")
    encoder.save_to_json(output_file)