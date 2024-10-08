from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B")  # Initialize the pipeline only once
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_response(prompt):
    response = generator(prompt, max_length=100, num_return_sequences=1)
    return response[0]["generated_text"]

if __name__ == "__main__":
    prompt = input("Enter a prompt: ")  # Get user input
    response = generate_response(prompt)
    print("Generated Response: ", response)
