# Quiz AI Application

This project is a web-based application that uses AI to generate and transcribe quizzes. It allows users to upload files, generate quiz questions, and transcribe audio into text.

## Project Structure

This repository is structured as follows:

- **`app.py`**  
  Entry point of the Flask application.

- **`config.yml`**  
  Contains configuration settings for the app.

- **`requirements.txt`**  
  Lists Python dependencies required to run the project.

- **`README.md`**  
  Documentation for understanding and setting up the project.

### `quiz_ai/` – Core Backend Logic
- **`__init__.py`**  
  Initializes the Python package.
- **`constants.py`**  
  Defines constant values used throughout the application.
- **`generate.py`**  
  Handles quiz generation from transcripts.
- **`transcribe.py`**  
  Manages transcription of uploaded audio or video.

### `templates/` – HTML Templates
- **`home.html`**  
  The landing page of the application.
- **`quiz.html`**  
  Displays the generated quiz content.
- **`upload.html`**  
  UI for uploading media or documents.

### `uploads/` – User Uploads
- **`<UUID>/`**  
  Stores uploaded files in session-specific folders using UUIDs.               

## Features

- **Quiz Generation**: Automatically generate quiz questions from uploaded files.
- **Audio Transcription**: Convert audio files into text using AI.
- **Web Interface**: User-friendly web interface for uploading files and viewing results.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. Set up a virtual environment:
    ```bash
    python -m venv quizEnv
    ### On Windows:
    quizEnv\Scripts\activate
    ### On Unix or MacOS:
    source quizEnv/bin/activate

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Configure the application:

    Update config.yml with your desired settings.

## Usage
1. Start the application using:   `python app.py`

2. Open your browser and navigate to http://localhost:port.
    (port number being specified)

3. Use the web interface to upload files or transcribe audio from video files and generate quizzes.

## Dependencies
 - Python 3.x
 - Flask
 - Other dependencies listed in requirements.txt

## Contributing?
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
AI models and libraries are used in this project so open-source contributors who made this project are possible.

### Note:
Save this content as `README.md` in the root directory of your project.
