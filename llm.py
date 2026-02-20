
from llama_cpp import Llama

llm = Llama(
    model_path="models/mistral-7b-instruct.gguf",
    n_ctx=2048,
    n_threads=4
)

def generate(prompt):
    output = llm(
        prompt,
        max_tokens=512,
        stop=["</s>"]
    )
    return output["choices"][0]["text"]
