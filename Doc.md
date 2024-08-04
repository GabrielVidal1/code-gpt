Sure, here's a brief overview of the different commands and examples:

### 1. General Project Overview

This project processes files in chunks according to specified types and utilizes AI models to generate responses or execute commands.

### 2. Command Descriptions

#### `Chunk` (Base Class)

- **File:** `src/parser/chunks/base_chunk.py`
- **Description:** Base class representing a generic data chunk.
- **Methods:** `__str__`, `__repr__`, `format`

#### `BashCommandChunk` (Bash Command)

- **File:** `src/parser/chunks/command.py`
- **Description:** Represents a bash command to execute.
- **Methods:** `format`, `process`
- **Example Data:** `>ls -la`
- **Example Usage:** Executes `ls -la` and stores the result.

#### `MentionChunk` (File Mention)

- **File:** `src/parser/chunks/mention.py`
- **Description:** Represents a reference to another file.
- **Methods:** `format`
- **Example Data:** `>@path/to/file.txt`
- **Example Usage:** Reads the content of `file.txt`.

#### `OutputChunk` (Output Handling)

- **File:** `src/parser/chunks/output.py`
- **Description:** Handles the output generated and writes it to a file.
- **Methods:** `format_prompt`, `format`, `output_to_file`
- **Example Data:** `>output.txt`
- **Example Usage:** Writes AI model response to `output.txt`.

### 3. Usage Example

Given a source file `source.txt` containing:

```plaintext
>Hello World
>!ls -la
>output.txt
```

- **Steps:**
  1. `parse_file` reads `source.txt` and identifies chunks.
  2. `BashCommandChunk` executes `ls -la`.
  3. `OutputChunk` writes results to `output.txt`.

### 4. Running the Main Script

```sh
python src/main.py --source_filename source.txt
```
