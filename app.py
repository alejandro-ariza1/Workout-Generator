from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
from flask import Flask, request, jsonify, render_template
import json

load_dotenv()
app = Flask (__name__)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/your-workout", methods=["POST"])
def generate():
    goal = request.form["goal"]
    experience = request.form["experience"]
    days = request.form["days"]
    time = request.form["time"]
    equipment = request.form["equipment"]

    prompt = f"""
    Create a workout plan based on the following information:

    Weight goal: {goal}
    Experience level: {experience}
    Days available per week: {days}
    Time available per workout: {time} minutes
    Equipment available: {equipment}

    Create a workout plan that fits these requirements.

    For each workout day, include:
    - Exercise name
    - Number of sets
    - Number of reps
    - Rest time
    - Nutrition advice for the weight goal

    Return ONLY valid JSON using this structure:
    {{
        "workout_plan": [
            {{
                "day": "Day 1",
                "focus": "Full Body",
                "exercises": [
                    {{
                        "name": "Exercise name",
                        "sets": 3,
                        "reps": "8-12",
                        "rest": "60 seconds"
                    }}
                ]
            }}
        ],
        "nutrition": 
            {{
            "advice": "Nutrition advice for the user's weight goal",
            "protein": "Protein recommendation",
            "calories": "Calorie guidance"
            }}
        ,
        "explanation": "Explain the workout and why it is suitable."
    }}

    Keep the response clear and easy to read.
    Give an explanation on explaining the workout and why it's good
    Give some advice and explanation on nutrition to help reach their weight goal
    """

    response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction="You are a workout generator. If asked about anything else, decline it",
        response_mime_type="application/json"
        )
    )
    workout = json.loads(response.text)
    return render_template("your-workout.html", workout=workout)


if __name__ == "__main__":
    app.run(debug=True)