from fastapi import FastAPI
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

app = FastAPI()

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B")
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

@app.post("/generate")
async def generate(prompt: str):
    response = generator(prompt, max_length=200, num_return_sequences=1)
    return {"response": response[0]["generated_text"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)