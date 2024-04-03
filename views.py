# chatbot/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from sklearn.model_selection import train_test_split
from .models import AyurvedicQuestion, UserResponse
import json

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from .models import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

data = {
    "Height": ["Short", "Normal", "Tall"],
    "Weight": ["Underweight", "Normal", "Overweight"],
    "Voice": ["Harsh", "Thin", "Heavy"],
    "Hair_colour": ["Grey", "Veryblack", "Normal"],
    "Iris_colour": ["Blue/dark Brown", "Black", "Brown"],
    "Pulse": ["Uncertain/Fast", "Normal", "Normal/Slow"],
    "Muscle": ["Thin", "Normal", "Fat/Thick"],
    "Tendom_reflex": ["Fast", "Moderate", "Slow"],
    "Pain_on_pressing": ["Maximum", "Moderate", "Low"],
    "Bones": ["Thin", "Normal", "Thick&Strong"],
    "Pulse_character": ["Leech", "Normal", "Pigeon/Swan"],
    "Sleeping_schedule": ["Less", "Normal", "Over"],
    "Temperament": ["Not in decisions", "Angry in decisions", "Constant in decisions"],
    "Power_level": ["Less", "Normal", "High"],
    "Body_Frame": ["Thin", "Moderate", "Thick/Strong"],
    "Skin": ["Dry/Cool", "Soft/Fair", "Thick/White"],
    "Hair": ["Dry/Easy to break", "Soft/Oily", "Thick/Wavy/Straight"],
    "Teeth": ["Big/Crooked", "SoftGums/Yellowish", "Strong/White"],
    "Eyes": ["Small/Dull", "Sharp/Shiny", "Big/Attractive"],
    "Preferred_taste": ["Salty/Sweet", "Bitter/Astringent", "Pungent/Astringent"],
    "Physical_activity": ["Very active", "Moderate", "Lethargic"],
    "Mindset_whole_day": ["Active/Nervous", "Aggressive/Analytical", "Slow/Dullness"],
    "Memory_power": ["Quick to understand", "Sharp", "Slow perceive but prolonged memory"],
    "Quality_of_Nails": ["Dry/Thin", "Soft/Pink", "Thick/Strong/Soft"],
    "Dosha": ["VATTA", "PITTA", "KAPPA"]
}
data=pd.DataFrame(data)
X = data.drop("Dosha", axis=1)
y = data["Dosha"]

# One-hot encode categorical features
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Choose a model and train it
model = RandomForestClassifier()
model.fit(X_train, y_train)

class AyurvedicChatbot:
    def __init__(self):
        # Load the dataset and train the model (Replace 'your_dataset.csv' with your actual dataset)
        self.df = pd.read_csv(
            r"C:\Users\Nandini\Djangoproject\myproject\chatbot\ayurdataset.csv"
        )

        # Extract questions and doshas from the dataset
        self.questions = self.df["Questions"]
        self.doshas = self.df[["VATTA", "PITTA", "KAPPA"]]

        # Convert text data to numerical features using CountVectorizer
        self.vectorizer = CountVectorizer()
        self.X_train_vec = self.vectorizer.fit_transform(self.questions)

        # Build and train the KNN model
        self.model = KNeighborsClassifier(n_neighbors=3)
        self.model.fit(self.X_train_vec, self.doshas)

    def ask_question(self, user_responses):
        # Vectorize the user responses
        user_input = " ".join(user_responses)
        question_vec = self.vectorizer.transform([user_input])

        # Predict the dosha using the trained model
        dosha_prediction = self.model.predict(question_vec)[0]

        return dosha_prediction


chatbot_instance = AyurvedicChatbot()

'''
def chatbot_home(request):
    if request.method == "POST":
        user_responses = [request.POST.get(f"question_{i}") for i in range(1, 6)]
        dosha_prediction = chatbot_instance.ask_question(user_responses)

        # Store user responses and dosha prediction in the database (customize as needed)
        UserResponse.objects.create(
            user=request.user,
            responses=user_responses,
            dosha_prediction=dosha_prediction,
        )

        return redirect("chatbot:chatbot_home")

    questions = AyurvedicQuestion.objects.all()
    return render(request, "chatbot/templates/chatbot/home.html", {"questions": questions})'''


def get_data(request):
    #if request.method == "GET":
    questions = AyurvedicQuestion.objects.all()
    print('line 69')
    return render(request, "chatbot/home.html", context={"questions": questions})
    

def save_data(request):

    if request.method == "POST":
        
        height = request.POST.get("1")
        weight = request.POST.get("2")
        voice = request.POST.get("3")
        hair_color = request.POST.get("4")
        iris_color = request.POST.get("5")
        pulse = request.POST.get("6")
        muscle = request.POST.get("7")
        tendom = request.POST.get("8")
        pain_on_pressing = request.POST.get("9")
        bones = request.POST.get("10")
        pulse_character = request.POST.get("11")
        sleeping_schedule = request.POST.get("12")
        temperament = request.POST.get("13")
        power_level = request.POST.get("14")
        body_frame = request.POST.get("15")
        skin = request.POST.get("16")
        hair = request.POST.get("17")
        teeth = request.POST.get("18")
        eyes = request.POST.get("19")
        preferred_taste = request.POST.get("20")
        physical_activity = request.POST.get("21")
        mindset_whole_day = request.POST.get("22")
        memory_power = request.POST.get("23")
        quality_of_nails = request.POST.get("24")
        user_answers={
            "Height": [height],
            "Weight": [weight],
            "Voice": [voice],
            "Hair_colour": [hair_color],
            "Iris_colour": [iris_color],
            "Pulse": [pulse],
            "Muscle": [muscle],
            "Tendom_reflex": [tendom],
            "Pain_on_pressing": [pain_on_pressing],
            "Bones": [bones],
            "Pulse_character": [pulse_character],
            "Sleeping_schedule": [sleeping_schedule],
            "Temperament": [temperament],
            "Power_level": [power_level],
            "Body_Frame": [body_frame],
            "Skin": [skin],
            "Hair": [hair],
            "Teeth": [teeth],
            "Eyes": [eyes],
            "Preferred_taste": [preferred_taste],
            "Physical_activity": [physical_activity],
            "Mindset_whole_day": [mindset_whole_day],
            "Memory_power": [memory_power],
            "Quality_of_Nails": [quality_of_nails]
        }
        # answer = model.ask_question([height,weight])
        # print(answer)
        # import pickle
        # with open("chatbot/model.pkl","rb") as f:
        #     print(f.read())
        # model = pickle.load("/chatbot/model.pkl")
        df1=pd.DataFrame(user_answers)
        # print(df1)
        # encoder = pickle.loads("/chatbot/encoder.pkl")
        answer = model.predict(encoder.transform(df1))
        
        # user_responses = []
        # for q, o in data.items():
        #     user_responses.append(o)
        # print('line 78')
        # # Predict dosha using the chatbot_instance
        # dosha_prediction = chatbot_instance.ask_question(user_responses)

        # # Store user responses and dosha prediction in the database
        # user = UserResponse.objects.create(user=request.user, dosha_prediction=dosha_prediction)
        # for q, o in data.items():
        #     user.option.add(AyurvedicOptions.objects.get(id=o))
        # user.save()
        # print('line 87')
        
        # '''    user = UserResponse.objects.create(user=request.user)
        # for q, o in data.items():
        #     user.option.add(o)
        # user.save()'''
        # print('line 92',dosha_prediction)
        # messages.success(request, 'Submitted Sucessfully')
    desc=""
    if answer == "PITTA":     
        desc ="Based on your responses, it seems that your dominant dosha is Pitta. To maintain Pitta prakriti, consider incorporating foods like cow's milk, cow ghee, split green gram, pomegranates, and Indian gooseberry into your daily diet. Utilize ingredients such as wheat, snake gourd, cabbage, and coriander leaves in your cooking. However, it's advisable to avoid stale and fermented foods, ice-creams and milkshakes of citrus fruits, smoking, tobacco, deep-fried items, pickles, non-vegetarian food (especially fish), and excessive consumption of salt and chilies. Opt for a diet that helps balance Pitta dosha for overall well-being." 
        print(desc)
    elif answer == "VATTA":
        desc ="Based on your responses, it appears that your dominant dosha is Vatta. To maintain Vatta prakriti, consider including daily foods such as green gram, milk, clarified butter, and warm water in your diet. Additionally, incorporate ingredients like garlic, bottle gourd, and whole wheat. Be cautious about consuming foods that may aggravate Vatta dosha, including green pea, bitter gourd, kidney beans, and cold beverages. If consuming these items, it's recommended to pair them with ghee, oil, buttermilk, or curd to balance Vatta dosha and prevent excessive aggravation."
        print(desc)
    else :
        desc ="Based on your responses, it appears that your dominant dosha is Kapha. To maintain Kapha prakriti, consider incorporating daily foods like honey, dried ginger, long pepper, and green gram into your diet. However, it's advisable to minimize the intake of curd, milk, sesame, sugar, and rice. Additionally, avoid day sleeping, refrain from excessive sweet and sour foods, and be cautious of cold beverages and cold environments. Regular physical exercise is recommended to balance Kapha dosha."
        print(desc)
        
    return render(request, "chatbot/home.html", context={"dosha_prediction": answer,"description":desc,
                                                             "submitted": True})


def load_data():
    questions = [
        {
            "options": [
                {"dosha": "vatta", "option": "Short"},
                {"dosha": "pitta", "option": "Normal"},
                {"dosha": "kappa", "option": "Tall"},
            ],
            "question": "Your Height?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Underweight"},
                {"dosha": "pitta", "option": "Normal"},
                {"dosha": "kappa", "option": "Overweight"},
            ],
            "question": "Your Weight?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Harsh"},
                {"dosha": "pitta", "option": "Thin"},
                {"dosha": "kappa", "option": "Heavy"},
            ],
            "question": "Your Voice?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Grey"},
                {"dosha": "pitta", "option": "Veryblack"},
                {"dosha": "kappa", "option": "Normal"},
            ],
            "question": "Your Hair colour?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Blue/dark Brown"},
                {"dosha": "pitta", "option": "Black"},
                {"dosha": "kappa", "option": "Brown"},
            ],
            "question": "Your Iris colour?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Uncertain/Fast"},
                {"dosha": "pitta", "option": "Normal"},
                {"dosha": "kappa", "option": "Normal/Slow"},
            ],
            "question": "Your Pulse?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Thin"},
                {"dosha": "pitta", "option": "Normal"},
                {"dosha": "kappa", "option": "Fat/ Thick"},
            ],
            "question": "Your Muscle?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Fast"},
                {"dosha": "pitta", "option": "Moderate"},
                {"dosha": "kappa", "option": "Slow"},
            ],
            "question": "Your Tendom reflex?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Maximum"},
                {"dosha": "pitta", "option": "Moderate"},
                {"dosha": "kappa", "option": "Low"},
            ],
            "question": "Your Pain on pressing?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Thin"},
                {"dosha": "pitta", "option": "Normal"},
                {"dosha": "kappa", "option": "Thick&Strong"},
            ],
            "question": "Your Bones?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Leech"},
                {"dosha": "pitta", "option": "Normal"},
                {"dosha": "kappa", "option": "Pigeon / Swan"},
            ],
            "question": "Your Pulse character?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Less"},
                {"dosha": "pitta", "option": "Normal"},
                {"dosha": "kappa", "option": "Over"},
            ],
            "question": "Your Sleeping schedule?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Not in decisions"},
                {"dosha": "pitta", "option": "Angry in decisions"},
                {"dosha": "kappa", "option": "Constant in decisions"},
            ],
            "question": "Your Temperament?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Less"},
                {"dosha": "pitta", "option": "Normal"},
                {"dosha": "kappa", "option": "High"},
            ],
            "question": "Your Power level?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Thin"},
                {"dosha": "pitta", "option": "Moderate"},
                {"dosha": "kappa", "option": "Thick/strong"},
            ],
            "question": "Your Body Frame?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Dry/cool"},
                {"dosha": "pitta", "option": "Soft/fair"},
                {"dosha": "kappa", "option": "Thick/white"},
            ],
            "question": "Your Skin?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Dry/easy to break"},
                {"dosha": "pitta", "option": "Soft/oily"},
                {"dosha": "kappa", "option": "Thick/wavy/straight"},
            ],
            "question": "Your Hair?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Big/crooked"},
                {"dosha": "pitta", "option": "SoftGums/yellowish"},
                {"dosha": "kappa", "option": "Strong/white"},
            ],
            "question": "Your Teeth?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Small/dull"},
                {"dosha": "pitta", "option": "Sharp/shiny"},
                {"dosha": "kappa", "option": "Big/Attractive"},
            ],
            "question": "Your Eyes?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Salty/sweet"},
                {"dosha": "pitta", "option": "Bitter/Astringent"},
                {"dosha": "kappa", "option": "Pungent/Astringent"},
            ],
            "question": "Your  Preffered taste?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Very active"},
                {"dosha": "pitta", "option": "Moderate"},
                {"dosha": "kappa", "option": "Lethargic"},
            ],
            "question": "Your Physical activity?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Active/nervous"},
                {"dosha": "pitta", "option": "Aggressive/analytical"},
                {"dosha": "kappa", "option": "Slow/dullness"},
            ],
            "question": "Your Mindset whole day?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Quick to understand"},
                {"dosha": "pitta", "option": "sharp"},
                {"dosha": "kappa", "option": "Slow percieve but prolonged memory"},
            ],
            "question": "Your Memory power?",
        },
        {
            "options": [
                {"dosha": "vatta", "option": "Dry/Thin"},
                {"dosha": "pitta", "option": "Soft/pink"},
                {"dosha": "kappa", "option": "Thick/strong/soft"},
            ],
            "question": "Your Quality of Nails?",
        },
    ]

    for data in questions:
        question = AyurvedicQuestion.objects.create(question=data["question"])
        for op in data["options"]:
            instance = AyurvedicOptions(
                option=op["option"],
                dosha=op["dosha"],
                question=question,
            )
            instance.save()


