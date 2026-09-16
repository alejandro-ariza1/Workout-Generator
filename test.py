from dotenv import load_dotenv
from google import genai
import os
from flask import Flask, request, jsonify, render_template

load_dotenv()


client = genai.Client()

print("Sending request...")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Say a fact about spiders"
)

print("Gemini says:")
print(response.text)
