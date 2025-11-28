import env
from util import call_text_model


def generate_descriptive_message(message: str) -> str:
    DESCRIPTIVE_PROMPT = (
        "Create a professional message and change the person based on following input and don't include intro or ending lines like sure here is your...: "
        f"{message}\n"
        "Must follow:\n"
        "The output must be exactly 2 lines. Each line should be clear. Try to put extra feelings or filler in it"
        "Do not use variables like [street name], [Your Name] etc"
    )
    model_response = call_text_model(DESCRIPTIVE_PROMPT, env.MODEL_FOR_IMPROVING_MESSAGES)
    return model_response