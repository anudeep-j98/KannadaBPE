import json
import re

def remove_emojis(text):
    # Emoji pattern covers most emojis
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & pictographs
        "\U0001F680-\U0001F6FF"  # Transport & map symbols
        "\U0001F700-\U0001F77F"  # Alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric shapes extended
        "\U0001F800-\U0001F8FF"  # Supplemental arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental symbols & pictographs
        "\U0001FA00-\U0001FA6F"  # Chess symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and pictographs extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # Enclosed characters
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r'', text)


def clean_text(text):
    """
    Clean Kannada text using comprehensive regex patterns
    """

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # Regex pattern to match URLs
    url_pattern = r'(https?://\S+|www\.\S+)'
    # Remove email addresses
    text = re.sub(email_pattern, '', text)
    # Remove URLs
    text = re.sub(url_pattern, '', text)
    # Clean up extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Remove all special characters (including @, ://, . etc)
    text = re.sub(r'[!@#$%^&*()_+\-=\[\]{};:"|<>/?.,\\]', '', text)
    
    # Remove English characters
    text = re.sub(r'[a-zA-Z]', '', text)
    
    # Remove numbers (both English and Kannada)
    text = re.sub(r'[0-9]', '', text)
    
    # Step 5: Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()

    text = remove_emojis(text)

    return text

# Load the tokenizer vocabulary
def load_tokenizer():
    with open('encoding/kannada_tokenizer.json', 'r', encoding='utf-8') as f:
        tokens = json.load(f)
        stoi = tokens['stoi']
        itos = {str(v): k for k, v in stoi.items()}
    return stoi, itos

def encode_text(text: str) -> str:
    """Convert text to token indices"""
    stoi, itos = load_tokenizer()
    try:
        tokens = []
        current_pos = 0
        while current_pos < len(text):
            # Try to match the longest possible token
            found = False
            for token_length in range(min(1, len(text) - current_pos), 0, -1):
                substr = text[current_pos:current_pos + token_length]
                if substr in stoi:
                    tokens.append(stoi[substr])
                    current_pos += token_length
                    found = True
                    break
            if not found:
                return f"Error: Unable to encode character at position {current_pos}"
        
        return str(tokens)
    except Exception as e:
        return f"Error encoding text: {str(e)}"

def decode_tokens(tokens: list) -> str:
    """Convert token indices back to text"""
    stoi, itos = load_tokenizer()
    try:
        if tokens == [] or tokens == "":
            return "Error: Empty input"
                
        result = ""
        for token in tokens:
            token_str = str(token)
            if token_str not in itos:
                return f"Error: Invalid token {token} as token not found"
            result += itos[token_str]
        return result
    except ValueError:
        return "Error: Invalid input format. Please enter numbers separated by commas"
    except Exception as e:
        return f"Error decoding tokens: {str(e)}"