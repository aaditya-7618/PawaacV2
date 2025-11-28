import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


def generate_caption(image_path):
    # start_time = time.time()

    if torch.backends.mps.is_available():
        device = torch.device("mps") # for mac
    elif torch.cuda.is_available():
        device = torch.device("cuda") # for GPUs
    else:
        device = torch.device("cpu") # for system without GPUs

    # load model & processor
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large", use_fast=True)
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to(device)

    # Load and preprocess image
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, return_tensors="pt").to(device)

    # Disable gradient calculations for speed
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=60, num_beams=3, do_sample=False)

    caption = processor.decode(out[0], skip_special_tokens=True)

    # end_time = time.time()
    # print(f"⏱️ Time taken: {end_time - start_time:.2f} seconds")

    return caption

# print(generate_caption(env.IMAGE_PATH4))