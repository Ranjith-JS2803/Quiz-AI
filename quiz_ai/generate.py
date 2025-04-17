from .constants import *

def convert_docx_to_txt(docx_path):
    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def generate_quiz(dir_path, filepaths):
    try:
        files = []
        for path in filepaths:
            # Convert docx to txt if necessary
            if path.endswith('.docx'):
                text = convert_docx_to_txt(path)
                txt_path = path.replace('.docx', '.txt')
                with open(txt_path, 'w') as f:
                    f.write(text)
                uploaded = genai.upload_file(txt_path)
            else:            
                uploaded = genai.upload_file(path)
            files.append(uploaded)
    except Exception as e:
        print(f"[ERROR] File upload failed: {e}")
        return []

    prompt = (
        "You are an AI tutor. Read the uploaded documents and generate a quiz.\n\n"
        "Respond in this format:\n"
        "[\n"
        "  {\"title\": \"<Generate a Title that depicts the uploaded content>\"},\n"
        "  {\"type\": \"MCQ\", \"question\": \"...\", \"options\": [\"Option A\", \"Option B\", \"Option C\", \"Option D\"], \"answer\": \"Option A\"},\n"
        "  {\"type\": \"MSQ\", \"question\": \"...\", \"options\": [\"Option A\", \"Option B\", \"Option C\", \"Option D\"], \"answer\": [\"Option A\", \"Option C\"]},\n"
        "  {\"type\": \"NAT\", \"question\": \"...\", \"answer\": 123}\n"
        "]\n"
        "Use only the content from the uploaded documents.\n"
        "Include as many quiz questions as possible.\n"
        "Each MCQ and MSQ must have exactly 4 options.\n"
        "Respond only with the JSON list — no explanations, comments, or formatting."
    )

    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        contents = [prompt] + files
        response = model.generate_content(contents=contents)

        quiz_json_str = response.text.strip()

        if quiz_json_str.startswith("```json"):
            quiz_json_str = quiz_json_str.lstrip("```json").rstrip("```").strip()
        
        output_path = os.path.join(dir_path, "quiz.json")
        with open(output_path, "w") as f:
            json.dump(json.loads(quiz_json_str), f, indent=4)
        return "Saved Quiz Questions as JSON!"

    except Exception as e:
        print(f"[ERROR] Gemini generation failed: {e}")
        return []