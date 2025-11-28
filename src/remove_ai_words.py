import re
def remove_ai_preface_lines(text: str) -> str:
    # Patterns matching entire lines that should be removed
    patterns = [
        r"^\s*sure.*$",                    # Sure...
        r"^\s*here\s+is.*$",               # Here is...
        r"^\s*here's.*$",                  # Here's...
        r"^\s*here\s+are.*$",              # Here are...
        r"^\s*as an ai.*$",                # As an AI...
        r"^\s*okay.*$",                    # Okay...
        r"^\s*ok.*$",                      # Ok...
        r"^\s*below is.*$",                # Below is...
        r"^\s*this is the message.*$",     # This is the message...
        r"^\s*your requested.*$",          # Your requested...
    ]

    cleaned_lines = []
    for line in text.splitlines():
        if any(re.match(p, line, flags=re.IGNORECASE) for p in patterns):
            continue  # skip the full line
        cleaned_lines.append(line)

    # Join again + remove extra blank lines
    cleaned = "\n".join(cleaned_lines)
    cleaned = re.sub(r"\n{2,}", "\n", cleaned).strip()
    return cleaned

# print(remove_ai_preface_lines("Sure, here is your alert:\n\n🚨 Emergency at [Street Name]! Please send help immediately!!!   \n\nThank you!"))
# print("\n")

# print(remove_ai_preface_lines("As an AI language model, I cannot provide the information you requested.\n\nHowever, please remember to stay safe!"))
# print("\n")

# print(remove_ai_preface_lines("Here is the message you asked for:\n\nThere is a fire at [Location]. Immediate assistance is needed.\n\nStay safe!"))
# print("\n")

# print(remove_ai_preface_lines("Okay, here is your alert:\n\n🚨 Emergency at [Street Name]! Please send help immediately!!!   \n\nThank you!"))
# print("\n")

# print(remove_ai_preface_lines("This is the message you requested:\n\nThere is a gas leak at [Location]. Evacuation is necessary.\n\nStay safe!"))
# print("\n")

# print(remove_ai_preface_lines("Your requested alert:\n\n🚨 Emergency at [Street Name]! Please send help immediately!!!   \n\nThank you!"))
# print("\n")

# print(remove_ai_preface_lines("Below is the alert you asked for:\n\nThere is a flood at [Location]. Immediate evacuation is advised.\n\nStay safe!"))
# print("\n")

# print(remove_ai_preface_lines("Ok, here is your alert:\n\n🚨 Emergency at [Street Name]! Please send help immediately!!!   \n\nThank you!"))
# print("\n")

# print(remove_ai_preface_lines("Here are the details you requested:\n\nThere is a chemical spill at [Location]. Please avoid the area.\n\nStay safe!"))
# print("\n")

# print(remove_ai_preface_lines("Sure, here is the 2-line message you requested:\n Birdwatching, a serene pastime, unfolds in the tranquil park as the serene observer witnesses nature's vibrant colors and melodies."))
# print("\n")