# Safety Talks Generator

This project is a Python application for generating safety talks using the Claude API (Haiku model). It features a Streamlit interface for easy interaction, multi-language support, and the ability to download generated safety talks.

## Features

1. Generate safety talks on any topic
2. Multi-language support (English, Spanish, French)
3. User-friendly Streamlit interface
4. Download generated safety talks as text files

## Prerequisites

- Python 3.7 or higher
- Claude API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/safety-talks-generator.git
   cd safety-talks-generator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory of the project and add your Claude API key:
   ```
   CLAUDE_API_KEY=your_actual_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run safety_talks_generator.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Enter a safety topic, select a language, and click "Generate Safety Talk" to create a new safety talk.

4. Use the "Download Safety Talk" button to save the generated talk as a text file.

## Security Note

The `.env` file containing your API key is included in `.gitignore` to prevent it from being committed to version control. Never share your API key publicly or commit it to your repository.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.