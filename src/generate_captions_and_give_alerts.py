from generate_captions_v2 import generate_caption
from improve_message import improve_message

def generate_alert_and_give_alert(image_path):
    # start_time = time.time()

    caption = generate_caption(image_path)
    improved_alert = improve_message(caption)

    # end_time = time.time()
    # print(f"⏱️ Time taken: {end_time - start_time:.2f} seconds\n")
    # print("Processing image:", image_path)
    print(improved_alert)
    print("\n")


# print(generate_alert_and_give_alert("/Users/aadi/Desktop/pawaac/images/040.jpg"))
