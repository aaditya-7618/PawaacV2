import re
from remove_ai_words import remove_ai_preface_lines

def clean_model_output(text: str) -> str:
    """
    Cleans LLM-generated alert text by removing placeholders like [Street Name]
    and the word immediately before it, then tidies punctuation and spacing.
    """

    # Remove the word before [placeholder] and the placeholder itself
    text = re.sub(r"\b\w+\s*\[.*?\]", "", text)

    # Remove leftover empty brackets (if any)
    text = re.sub(r"\[.*?\]", "", text)

    # Remove unwanted symbols like '*'
    text = text.replace('*', '')

    # Fix double spaces or stray punctuation (like "at ." or " !")
    text = re.sub(r"\s+[.?!]", lambda m: m.group(0).strip(), text)
    text = re.sub(r"\s{2,}", " ", text)

    # Remove extra blank lines
    text = "\n".join(line.strip() for line in text.splitlines() if line.strip())

    # Optional: Clean up if a sentence ends with an orphan preposition (like "at." or "in.")
    text = re.sub(r"\b(at|in|on|near|around)\s*[.?!]", ".", text, flags=re.IGNORECASE)

    # Remove extra punctuation repeats (like "!!" → "!")
    text = re.sub(r"([!?])\1+", r"\1", text)

    return text.strip()


# print(clean_model_output("Sure, here is your alert:\n\n🚨 Emergency at [Street Name]! Please send help immediately!!!   \n\nThank you!"))

















# def clean_model_output(text: str) -> str:
#     """
#     Cleans LLM-generated alert text by removing placeholders like [Street Name]
#     and the word immediately before it, then tidies punctuation and spacing.
#     """
#     cleaned_text = text

#     # Remove the word before [placeholder] and the placeholder itself
#     cleaned_text = re.sub(r"\b\w+\s*\[.*?\]", "", cleaned_text)

#     # Remove leftover empty brackets (if any)
#     cleaned_text = re.sub(r"\[.*?\]", "", cleaned_text)

#     # Remove unwanted symbols like '*'
#     cleaned_text = cleaned_text.replace('*', '')

#     # Fix double spaces or stray punctuation (like "at ." or " !")
#     cleaned_text = re.sub(r"\s+[.?!]", lambda m: m.group(0).strip(), cleaned_text)
#     cleaned_text = re.sub(r"\s{2,}", " ", cleaned_text)

#     # Remove extra blank lines
#     cleaned_text = "\n".join(line.strip() for line in cleaned_text.splitlines() if line.strip())

#     # Optional: Clean up if a sentence ends with an orphan preposition (like "at." or "in.")
#     cleaned_text = re.sub(r"\b(at|in|on|near|around)\s*[.?!]", ".", cleaned_text, flags=re.IGNORECASE)

#     # ✅ Handle emojis (keep variation selector intact)
#     emoji_pattern = r"(?:🚨|⚠️|🔥|💥|🚑|🚒|✅|❌|🆘)"
#     # Add space before emoji if not at start and no space before
#     cleaned_text = re.sub(rf"(?<!\s)({emoji_pattern})", r" \1", cleaned_text)
#     # Add space after emoji if not followed by space or end
#     cleaned_text = re.sub(rf"({emoji_pattern})(?!\s|$)", r"\1 ", cleaned_text)

#     # Remove extra punctuation repeats (like "!!" → "!")
#     cleaned_text = re.sub(r"([!?])\1+", r"\1", cleaned_text)

#     return cleaned_text.strip()

