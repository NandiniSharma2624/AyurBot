from pprint import pprint

questions_data = [
    "Your Height?,Short,Normal,Tall",
    "Your Weight?,Underweight,Normal,Overweight",
    "Your Voice?,Harsh,Thin,Heavy",
    "Your Hair colour?,Grey,Veryblack,Normal",
    "Your Iris colour?,Blue/dark Brown,Black,Brown",
    "Your Pulse?,Uncertain/Fast,Normal,Normal/Slow",
    "Your Muscle?,Thin,Normal,Fat/ Thick",
    "Your Tendom reflex?,Fast,Moderate,Slow",
    "Your Pain on pressing?,Maximum,Moderate,Low",
    "Your Bones?,Thin,Normal,Thick&Strong",
    "Your Pulse character?,Leech,Normal,Pigeon / Swan",
    "Your Sleeping schedule?,Less,Normal,Over",
    "Your Temperament?,Not in decisions,Angry in decisions,Constant in decisions",
    "Your Power level?,Less,Normal,High",
    "Your Body Frame?,Thin,Moderate,Thick/strong",
    "Your Skin?,Dry/cool,Soft/fair,Thick/white",
    "Your Hair?,Dry/easy to break,Soft/oily,Thick/wavy/straight",
    "Your Teeth?,Big/crooked,SoftGums/yellowish,Strong/white",
    "Your Eyes?,Small/dull,Sharp/shiny,Big/Attractive",
    "Your  Preffered taste?,Salty/sweet,Bitter/Astringent,Pungent/Astringent",
    " Your Physical activity?,Very active,Moderate,Lethargic",
    "Your Mindset whole day?,Active/nervous,Aggressive/analytical, Slow/dullness",
    "Your Memory power?,Quick to understand,sharp,Slow percieve but prolonged memory",
    "Your Quality of Nails?,Dry/Thin,Soft/pink,Thick/strong/soft",
]

converted_data = []

for question_string in questions_data:
    question, *options = map(str.strip, question_string.split(","))

    question_data = {
        "question": question,
        "options": [
            {"option": option, "dosha": index + 1}
            for index, option in enumerate(options)
        ],
    }

    converted_data.append(question_data)

# Printing the converted format
pprint(converted_data)

