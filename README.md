# Student Learning Book Creator

This Python script facilitates the creation of educational books aimed at helping students study better and more efficiently. By leveraging AI assistance, the tool generates comprehensive Microsoft Word documents based on user-defined topics and students' educational backgrounds.

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python)
- `docx` library (install using `pip install python-docx`)
- `g4f` library (install using `pip install g4f`)
- An internet connection for AI assistance

## Usage

1. **Running the Script:**
   - Execute the script by running the `main()` function within the Python environment.
   - The script launches a user-friendly graphical interface (GUI) to guide you through the book creation process.

2. **Entering Book Details:**
   - Input the topic of the educational book in the designated field.
   - Select the appropriate student experience level from the available options (Elementary School, Middle School, High School, University).

3. **Initiating Book Creation:**
   - Click the "Start Book Creation" button to commence the book generation process.
   - The script employs AI assistance to craft the book's outline and content, tailored to the specified topic and students' educational levels.
   - Upon completion, a confirmation message will signify the successful creation of the book.

4. **Output:**
   - The generated Microsoft Word document will be saved in the current directory, with the sanitized book title serving as the filename.

## Notes

- Ensure a stable internet connection during book creation for AI assistance.
- Supported image formats for the cover picture include `.jpg`, `.jpeg`, `.png`, and `.gif`.
- The book's outline and content are dynamically generated based on the provided topic and students' educational backgrounds.
- The generated educational content aims to enhance student learning experiences by catering to their educational levels.
