from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import env

# set device (use GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"

# load the BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", use_fast=True)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

# load your image
image = Image.open(env.IMAGE_PATH1).convert("RGB") # replace with your image path

# prepare the image for the model
inputs = processor(images=image, return_tensors="pt").to(device)

# generate the caption
out = model.generate(**inputs)

# decode the output to get readable text
caption = processor.decode(out[0], skip_special_tokens=True)

print("Generated Caption:", caption)