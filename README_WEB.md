# VIP-CLI Web Chat Interface

A web-based chat interface for the VIP-CLI AI Assistant using Flask and the LLM library.

```bash
git clone https://github.com/Automattic/vip-cli-llm.git
```

<img width="1573" alt="Screenshot 2025-05-30 at 18 12 29" src="https://github.com/user-attachments/assets/ffa062d3-9428-4850-8134-99322794e0bb" />

## Features

- Modern, responsive chat interface
- Real-time message updates
- Typing indicators
- Error handling
- Markdown support (via LLM responses)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure your environment variables are set:
   ```bash
   # .env file
   OPENAI_API_KEY=your_api_key_here
   ```

3. Make sure your context files are in place:
   - `context/vip-cli-context.txt`
   - `context/vip-cli-instructions.txt`

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/         # HTML templates
│   └── index.html    # Chat interface template
└── context/          # LLM context files
    ├── vip-cli-context.txt
    └── vip-cli-instructions.txt
```

## Customization

- Modify the UI by editing `templates/index.html`
- Adjust the LLM model and fragments in `app.py`
- Add additional routes or features as needed

## Notes

- The application uses Flask's development server by default
- For production, use a proper WSGI server like Gunicorn
- Consider adding authentication for production use 
