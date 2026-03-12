import gradio as gr
import os
import groq
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=key)

def summarize(text):

    if not text.strip():
        return "Please enter text to summarize"
    
    try:
        messages = [
            {"role": "system", "content": "You need to summarize the input, make sure the length is not greater than 150 and you need to give bullet points"},
            {"role": "user", "content": text}
        ]
        
        response = client.chat.completions.create(
            model = "llama-3.1-8b-instant",
            messages = messages
        )
        return response.choices[0].message.content
    except groq.AuthenticationError:
        return "Invalid API key"
    except groq.RateLimitError:
        return "Too many requests, try again"
    except Exception as e:
        return "Error: " + str(e)
        

# Gradio interface
iface = gr.Interface(
    fn = summarize,
    inputs=gr.Textbox(lines=8, placeholder="Paste your article/text here...", label="Input Text"),
    outputs=gr.Textbox(label="Summary"),
    title="AI Text Summarizer",
    description = "Powered by Groq/LLaMA"
)

if __name__ == "__main__":
    iface.launch()



