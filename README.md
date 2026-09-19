# AI Workout-Generator

A simple Flask web app that generates a personalized workout plan and nutrition advice using Google's Gemini API, based on user-submitted preferences.

## Features

- Collects the user's weight goal, experience level, available days per week, time per workout, and available equipment via a form
- Sends this information to Gemini to generate a structured, personalized workout plan
- Returns the plan as JSON and renders it in a clean, grid-based layout
- Displays exercises grouped by day, along with an explanation of the plan and tailored nutrition advice

## Tech Stack

- **Backend:** Python, Flask
- **AI:** Google Gemini API (`google-genai` SDK)
- **Frontend:** Jinja2 templates, HTML/CSS
- **Config:** `python-dotenv` for environment variables

## Project Structure

```
.
├── app.py                  # Flask app and Gemini integration
├── templates/
│   ├── home.html           # Input form for workout preferences
│   └── your-workout.html   # Displays the generated workout plan
├── static/
│   └── your-workout.css    # Styling for the results page
└── .env                    # Environment variables (not committed)
```

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Install dependencies**
   ```bash
   pip install flask google-genai python-dotenv
   ```

3. **Add your Gemini API key**

   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

   The app will be available at `http://127.0.0.1:5000`.

## How It Works

1. User fills out a form on the home page with their goal, experience level, available days, session length, and equipment.
2. On submit, the `/your-workout` route builds a prompt from this input and sends it to Gemini, requesting a strict JSON response.
3. Gemini's response is parsed and rendered into the results page, showing:
   - A day-by-day breakdown of exercises (sets, reps, rest)
   - An explanation of why the plan suits the user's goals
   - Nutrition guidance (general advice, protein, and calorie targets)

## Notes

- The Gemini system instruction restricts the model to workout related responses only.
- `response_mime_type="application/json"` is used to encourage a reliably parseable response, but you should still handle malformed JSON gracefully in production (e.g. wrap `json.loads` in a try/except).
- Remember to keep `debug=True` off in any production deployment.

## Possible Improvements

- Handle Gemini API errors and malformed JSON responses with user-facing error messages
- Add a loading state while the workout is being generated
- Let users save or export their generated workout plan