# CodeGPT Automation Project

## Overview

This project is designed to automate the process of interacting with the OpenAI API to process files. The script reads a source file, processes it through the OpenAI API (or optionally through Ollama), and writes the output to a target file. The project is equipped with various options to customize the behavior of the processing.

## Features

- **File Processing**: Reads a source file and processes its content through the specified client.
- **Client Options**: Choose between OpenAI or Ollama APIs.
- **Model Configuration**: Allows specifying a model, with `gpt-4o` as the default.
- **Debug Mode**: Option to enable or disable debug information.
- **Target File Management**: Optionally specify a target file for the output.

## Prerequisites

- Python 3.7+
- An OpenAI API key or access credentials for Ollama

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/code-gpt-automation.git
    cd code-gpt-automation
    ```

2. Create a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up your API keys/credentials for OpenAI or Ollama.

## Usage

Here's the basic usage of the script:

```sh
python src/main.py [-h] [--no-debug] [--client {openai,ollama}] [--model MODEL] source_filename [target_filename]
```

### Arguments

- `source_filename` (str): Source file to read from
- `target_filename` (str, optional): Target file to write to (optional)
- `--no-debug`: Disable writing debug information to a file
- `--client` (str): Client to use for processing (default: `openai`)
- `--model` (str): Model to use for processing (optional, default: `gpt-4o`)

### Example

```sh
python src/main.py my_source_file.txt my_target_file.txt --client=openai --model=gpt-3.5
```

## Project Structure

```plain
code-gpt-automation/
│
├── src/
│   ├── __init__.py
│   ├── args_parser.py
│   ├── main.py
│   ├── clients/     # Client-specific modules
│   ├── prompts/     # Predefined prompts
│   ├── system_prompt.py
│   ├── postprocess_chunks.py
│   ├── process.py
│   └── prompt_parser.py
├── requirements.txt
└── README.md (You are here!)
```

## Contributing

We welcome contributions! Please feel free to submit issues, fork the repository and create pull requests.

## License

This project is open-source and available under the MIT License.

## Contact

If you have any questions, feel free to reach out at [your-email@example.com].