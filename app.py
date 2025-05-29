from flask import Flask, render_template, request, jsonify
import llm
import os
from dotenv import load_dotenv
import html

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize LLM with your fragments
model = llm.get_model("gpt-4.1")

#model.add_fragment("vip-cli", "context/vip-cli-context.txt")
#model.add_fragment("instructions", "context/vip-cli-instructions.txt")

def clean_response(text):
    """Remove markdown code block markers from the response."""
    return text.replace('```html', '').replace('```', '').strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    try:
        # Get response from LLM
        response = model.prompt(
            user_message,
            fragments=[
                open("context/vip-cli-instructions.txt").read(), 
                open("context/vip-cli-context.txt").read(),
                "Response Instructions: Send response in HTML format with proper formatting. Use <pre> tags for code blocks and <code> for inline code."
            ]
        )
        
        # Get the response text and clean it
        response_text = clean_response(response.text())
        print(f"Response: {response_text}")
        
        return jsonify({
            'response': response_text,
            'status': 'success',
            'is_html': True
        })
    except Exception as e:
        # Print detailed error to console
        print(f"Error in chat route: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        print("Full traceback:")
        print(traceback.format_exc())
       
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 