from cleaning_alert import clean_model_output
from generate_descriptive_message import generate_descriptive_message
from get_message_type import get_message_type
from remove_ai_words import remove_ai_preface_lines
from sanitize_model_output import robust_model_output
import util

def improve_message(text_message):

    message_type = get_message_type(text_message)
    message = message_type + " : " + text_message
    res = generate_descriptive_message(message)
    res = robust_model_output(res)
    res = clean_model_output(res)
    res = util.split_into_new_lines(res)
    final_alert = remove_ai_preface_lines(res)

    str = ""
    if message_type == "Critical":
        str += "🚨 CRITICAL ALERT 🚨\n"
    else: 
        str += "🟢 NORMAL UPDATE 🟢 \n"

    capitalized_alert = text_message[0].upper() + text_message[1:]
    if util.normalize(capitalized_alert) not in util.normalize(final_alert):
        str += capitalized_alert+"\n"

    str += final_alert

    # print(str)
    # print("\n")
    return str



# improve_message("there is a red car that has crashed into the side of the road")
# improve_message("Someone is pointing a gun at another person in a crowded area")
# improve_message("Many vehicles are stuck in traffic on the highway due to an accident")
# improve_message("Few vehicles are parked on the side of the road")
# improve_message("Empty street with no activity")
# improve_message("A person is lying motionless on the ground in a public park")
# improve_message("A group of people are gathered peacefully in a public square")
# improve_message("A small fire has started in a trash bin on the sidewalk")
# improve_message("A cyclist has fallen off their bike on a busy street")
# improve_message("A dog is running loose in a residential neighborhood")
# improve_message("A person is jogging alone in a quiet park")
# improve_message("A street performer is entertaining a small crowd on the sidewalk")
# improve_message("A car is parked illegally in a no-parking zone")
# improve_message("A person is sitting alone on a bench in a public park")
# improve_message("A group of children are playing soccer in an open field")
# improve_message("A person is walking their dog in a residential area")          
# improve_message("A person is reading a book in a quiet library")
# improve_message("A person is waiting at a bus stop on a busy street")
# improve_message("A person is taking photographs of a scenic view in a park")
# improve_message("A person is painting a mural on a public wall in an urban area")       
# improve_message("A person is skateboarding in a public skate park")
# improve_message("A person is flying a kite in an open field on a windy day")
# improve_message("A person is gardening in their backyard on a sunny day")
# improve_message("A person is fishing by a calm lake in a peaceful setting")
# improve_message("A person is hiking on a nature trail in a forested area")
# improve_message("A person is birdwatching in a quiet park")
# improve_message("A person is meditating in a serene garden setting")
# improve_message("A person is practicing yoga on a mat in a tranquil park")      
# improve_message("A person is having a picnic in a sunny park")
# improve_message("Car is burning on the side of the road")
# improve_message("Person is unconscious on the sidewalk")
# improve_message("There is a fight happening between two people in a public area")
# improve_message("A building is on fire in a residential neighborhood")
# improve_message("There is a large crowd gathered in a public square")
