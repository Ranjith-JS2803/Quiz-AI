import yaml
import os
import json
from docx import Document
from moviepy.editor import VideoFileClip

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

import assemblyai as aai
aai.settings.api_key = config["AssemblyAI API"]

import google.generativeai as genai # pyright: ignore[reportMissingImports]
genai.configure(api_key=config["Gemini API"])