1. **BashCommandChunk**:

   - **Purpose**: Run a bash command and return the output.
   - **Usage**:
     ```
     /tree -L 3
     ```
   - **Example**:
     ```python
     chunk = BashCommandChunk("/tree -L 3")
     print(chunk.format())
     ```

2. **MentionChunk**:

   - **Purpose**: Mention a file and return its content.
   - **Usage**:
     ```
     @file.txt
     ```
   - **Example**:
     ```python
     chunk = MentionChunk("@file.txt")
     print(chunk.format())
     ```

3. **OutputChunk**:
   - **Purpose**: Output the current chunk content to a file.
   - **Usage**:
     ```
     >file.txt
     ```
   - **Example**:
     ```python
     chunk = OutputChunk(">file.txt")
     chunk.output_to_file("This is the content.")
     print(chunk.format())
     ```
