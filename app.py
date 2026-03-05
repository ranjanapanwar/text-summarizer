import gradio as gr
from transformers import T5Tokenizer, T5ForConditionalGeneration

#Load T5 model 
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

def summarize(text):
    if not text.strip():
        return "Please enter text to summarize"
    
    # Preprocess with "summarize: " prefix
    inputs = tokenizer.encode("summarize: "+ text, 
                              return_tensors="pt",
                              max_length=512,
                              truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs, 
                                 max_length=150,
                                 min_length=30,
                                 num_beams=4,
                                 length_penalty=2.0,
                                 early_stopping=True) 
    
    summary = tokenizer.decode(summary_ids[0],
                               skip_special_tokens=True)
    
    return summary

# Gradio interface
iface = gr.Interface(
    fn = summarize,
    inputs=gr.Textbox(lines=8, placeholder="Paste your article/text here...", label="Input Text"),
    outputs=gr.Textbox(label="Summary"),
    title="AI Text Summarizer (T5)",
    description = "Powered by google's T5-small model"
)

if __name__ == "__main__":
    iface.launch()



