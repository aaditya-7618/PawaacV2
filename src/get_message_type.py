import re
import env
from util import call_text_model


CRITICAL_KEYWORDS = [
    # 🔫 Violence & Weapons
    "gun", "knife", "weapon", "shoot", "shooting", "stab", "stabbing",
    "attack", "assault", "fight", "fighting", "riot", "hostage",
    "threat", "terror", "bomb", "blast", "explosion",

    # 🔥 Fire & Hazards
    "fire", "burning", "smoke", "gas leak", "fuel leak",
    "chemical", "toxic", "hazard", "radiation", "short circuit",

    # 🚑 Medical Emergencies
    "unconscious", "collapsed", "bleeding", "injured", "injury",
    "dead", "death", "cardiac", "heart attack", "seizure",
    "not breathing", "overdose",

    # 🚗 Road & Transport Disasters
    "crash", "accident", "collision", "pileup", "overturned",
    "run over", "derailed", "smoke", "crash", "collapse", "crashed", "busy street", "busy road",

    # 🌊 Natural Disasters
    "earthquake", "flood", "cyclone", "hurricane", "tsunami",
    "landslide", "avalanche", "wildfire", "storm",

    # 🐕 Dangerous Animals
    "dog attack", "snake bite", "wild animal", "tiger",
    "leopard", "bear attack", "rabid",

    # 🏢 Structural Failures
    "building collapse", "roof collapse", "wall collapse", "collapse",
    "power line down", "electric shock",

    #Misc
    "lying motionless", "unconscious", "person down", "motionless person", "blood",
    "injury", "illegally", "crowd", "protest", "march",
]

NON_CRITICAL_KEYWORDS = [
    # 🚶 Normal Human Activities
    "walking", "jogging", "running", "sitting", "standing", "waiting",
    "talking", "chatting", "reading",

    # 🌳 Leisure & Recreation
    "picnic", "gardening", "fishing", "birdwatching",
    "skateboarding", "cycling", "hiking", "yoga", "meditating",
    "playing", "football", "cricket", "soccer", "kite",

    # 🎭 Public & Cultural
    "street performer", "music", "dancing", "mural", "painting",
    "photograph", "photography", "shooting photos",

    # 🚗 Traffic (Non-Danger)
    "parked", "parking", "slow traffic", "traffic jam", "waiting signal",

    # 👨‍👩‍👦 Public Presence
    "crowd", "gathered", "group", "protest", "march",

    # 🏠 Safe Locations
    "library", "park", "garden", "bench", "field", "playground",
    "bus stop", "station"
]

def get_message_type(text_message: str) -> str:
    # TODO - Create a logic to include the critical keywords with breaks like
    # 1. Critical : A person is waiting at a bus stop on a busy street
    # 2. Critical : A street performer is entertaining a small crowd on the sidewalk
    text = text_message.lower()
    for word in CRITICAL_KEYWORDS:
        if re.search(rf"\b{re.escape(word)}\b", text):
            return "Critical"
    return "Non-Critical"





# Needs work
def get_message_type_Needs_Modifcation(text_message: str) -> str:
    # TODO - may be use a better model and use this approach

    MESSAGE_TYPE_PROMPT = f"""
        You are an expert incident analyst. Your task is to classify the severity level of the following situation: "{text_message}"
        Use the following definitions:

        HIGH SEVERITY: Critical, dangerous, or life-threatening situations, Involves weapons, fire, explosions, fuel leaks, severe injuries, or immediate threats to people.
        Examples: someone pointing a gun, fights, major fire, vehicle explosion, hazardous spill.

        MEDIUM SEVERITY: Noticeable issue causing disruption or potential risk, May involve an accident or blockage, but some extant of life-threatening danger.
        Examples: traffic jam due to an accident, minor injuries, car crash or moderate roadside incidents.

        LOW SEVERITY: Harmless situations, No immediate danger, no injuries, no active threats.
        Examples: parked vehicles, slow traffic, small disturbances.

        Rules:
        - Respond with ONLY the severity label.
        - No explanation, Nothing just level.
        - Do not add extra words.
    """

    PROMPT_TWO_CLASSES = f"""Task: You are an expert incident analyst. Classify the severity level of the following situation: "{text_message}", using only these two classes: Critical and Non-Critical.
        Severity Classes:
        CRITICAL: All suitation that pose an immediate threat to life, safety, or property. Examples include active violence, fires, explosions, severe injuries,accident, suffering or hazardous material spills.

        NON-CRITICAL: Situations that do not pose an immediate threat to life, safety, or property. Examples include parked vehicles, minor disturbances, slow traffic, or non-emergency situations.  
             
        Rules:
        - Respond with ONLY the severity label.
        - No explanation. No extra words. Only one label.
        """
    
    Prompt = f"""
            You are an expert emergency incident analyst.
            Classify the severity of the following situation: "{text_message}"

            ONLY choose one of these two labels:
            CRITICAL:
            - Immediate danger to human life or major property
            - Examples:
            - Gun, knife, violence, fighting
            - Fire, explosion, burning vehicle/building
            - Serious accident with injury
            - Person unconscious, bleeding, or lying motionless
            - Dangerous animal attacking
            - Vehicle crash blocking traffic with injuries

            NON-CRITICAL:
            - No immediate danger to life or property
            - Examples:
            - Parked vehicles
            - People walking, jogging, skating, hiking, gardening, picnic
            - Street performer, photography, mural painting
            - Traffic without injury
            - Peaceful crowds or gatherings
            - Normal public activities

            IMPORTANT RULES:
            - Respond with ONLY ONE WORD: Critical OR Non-Critical
            - No explanations
            - No extra words
        """

    # model_response = call_text_model(MESSAGE_TYPE_PROMPT)
    model_response = call_text_model(Prompt, env.MODEL_FOR_IMPROVING_MESSAGES)
    text = model_response.lower()

    if "non" in text:
        return "Non-Critical"
    elif "Non" in text:
        return "Non-Critical"
    elif "NON" in text:
        return "Non-Critical"
    return "Critical"

    # high_keywords = ["high", "critical", "severe", "emergency", "urgent"]
    # medium_keywords = ["medium", "moderate", "warning"]

    # # Check medium severity
    # if any(word in text for word in medium_keywords):
    #     return "Medium Severity Incident"
    # # Check high severity first
    # if any(word in text for word in high_keywords):
    #     return "High Severity Emergency"
    # # Default to low severity (or explicit low match)
    # return "Low Severity Event"

