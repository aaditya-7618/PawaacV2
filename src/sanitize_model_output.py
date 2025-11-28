## Sanitizes model output by detecting AI refusal patterns and replacing them.
## transform the negative AI generated lines which is not required like 'unable to generate' or 'cannot generate' or 'I prioritize safety' etc

def robust_model_output(caption: str) -> str:
    # Comprehensive list of AI refusal keywords and patterns
    refusal_keywords = [
        # Direct refusals
        "unable to generate",
        "cannot generate",
        "can't generate",
        "i cannot",
        "i can't",
        "i am unable",
        "i'm not able",
        "i'm unable",
        "i'm unable",
        
        # Safety-related refusals
        "i prioritize safety",
        "prioritize safety",
        "against my guidelines",
        "against my values",
        "ethical guidelines",
        "content policy",
        
        # Apologetic refusals
        "i apologize",
        "i'm sorry, but i",
        "sorry, but i",
        "unfortunately, i cannot",
        
        # Harmful content mentions
        "harmful content",
        "inappropriate content",
        "dangerous content",
        "violates policy",
        "against policy",
        
        # AI acknowledgment phrases (when used in refusal context)
        "as an ai",
        "as a language model",
        "as an artificial intelligence"
    ]

    lower_caption = caption.lower()
    str = "This situation indicates a possible emergency that requires immediate human attention. Prompt action is recommended to assess and manage any potential risk"
    
    # Check if any refusal keyword is present
    for keyword in refusal_keywords:
        if keyword in lower_caption:
            # Return emergency alert instead of the refusal message
            return str
    # If no refusal patterns detected, return the original caption (stripped)
    return caption.strip()

# print(robust_model_output("I'm not able to generate messages about potentially dangerous situations or situations that could put people at risk."))
