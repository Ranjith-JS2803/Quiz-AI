# Quiz AI Application

This project is a web-based application that uses AI to generate and transcribe quizzes. It allows users to upload files, generate quiz questions, and transcribe audio into text.

## Project Structure
quiz-ai-app/
├── app.py                   
├── config.yml               
├── requirements.txt         
├── quiz_ai/                 
│   ├── __init__.py          
│   ├── constants.py         
│   ├── generate.py          
│   ├── transcribe.py        
│   └── __pycache__/         
├── quizEnv/                 
│   ├── pyvenv.cfg
│   ├── Include/
│   ├── Lib/
│   └── Scripts/
├── templates/               
│   ├── home.html
│   ├── quiz.html
│   └── upload.html
├── uploads/                 
│   └── <UUID>/              
└── README.md                

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