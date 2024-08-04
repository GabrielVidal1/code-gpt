def get_client(client_name, debug=False, model=None):
    if client_name == "openai":
        from .openai_client import OpenAIClient

        return OpenAIClient(debug, model if model else "gpt-4o")
    elif client_name == "ollama":
        from .ollama_client import OllamaClient

        return OllamaClient(debug, model if model else "mistral")
    else:
        raise ValueError(f"Unknown client: {client_name}")
