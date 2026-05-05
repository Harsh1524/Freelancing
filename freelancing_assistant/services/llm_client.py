import ollama
from config import OLLAMA_MODEL


def chat(prompt: str, system: str = "") -> str:
    """
    Single entry point for all Ollama/Qwen calls.
    All services call this function — never import ollama directly elsewhere.
    """
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    try:
        response = ollama.chat(model=OLLAMA_MODEL, messages=messages)
        return response["message"]["content"]
    except Exception as e:
        return (
            f"❌ **Ollama Error:** {e}\n\n"
            f"> Make sure Ollama is running: `ollama serve`\n"
            f"> Pull the model: `ollama pull {OLLAMA_MODEL}`"
        )