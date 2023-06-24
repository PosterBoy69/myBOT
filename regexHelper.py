import re


def remove_hashtags(text):
    # Remove all hashtags
    processed_text = re.sub(r'#\w+', '', text)
    return processed_text


def remove_portrait(text):
    # Remove the word "portrait" with all possible cases
    processed_text = re.sub(r'\bportrait\b', '', text, flags=re.IGNORECASE)
    return processed_text


def remove_special_characters(text):
    # Remove all special characters and emojis except '&', ':'
    processed_text = re.sub(r'[^\w\s&():]', '', text, flags=re.UNICODE)
    return processed_text


def remove_languages(text):
    # Remove HIN, TEL, MAL, ENG in all cases
    processed_text = re.sub(
        r'\b(HIN|TEL|MAL|ENG|TAM|HINDI|ENGLISH|TAMIL|TELUGU|MALYALAM|GUJARATI|KANNADA|KAN|GUJ|MARATHI|MAR|BENGALI|BEN)\b',
        '', text, flags=re.IGNORECASE)
    return processed_text


unallowedItems = [':', '[', ']', '(', ')', '  ']


def removeInvalidChars(text: str):
    # text = "Who Killed Sara?"
    text = remove_hashtags(text)
    text = remove_portrait(text)
    text = remove_special_characters(text)
    text = remove_languages(text)
    for unallowdItem in unallowedItems:
        text = text.replace(unallowdItem, '')
    return text.strip()


def detect_patterns(text):
    # Check if any hashtags are present
    if re.search(r'#\w+', text):
        return True

    # Check if the word "portrait" with any case is present
    if re.search(r'\bportrait\b', text, flags=re.IGNORECASE):
        return True

    # Check if any special characters or emojis (except '(', ')', and ':') are present
    if re.search(r'[^\w\s&():]', text, flags=re.UNICODE):
        return True

    # Check if HIN, TEL, MAL, ENG in any case are present
    if re.search(
            r'\b(HIN|TEL|MAL|ENG|TAM|HINDI|ENGLISH|TAMIL|TELUGU|MALYALAM|GUJARATI|KANNADA|KAN|GUJ|MARATHI|MAR|BENGALI|BEN)\b',
            text, flags=re.IGNORECASE):
        return True
    return False
