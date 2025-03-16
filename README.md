AI Video Summarizer

https://github.com/user-attachments/assets/5b6c68a4-86ff-4828-badd-116310d47175


Description
AI Video Summarizer is a desktop application that automatically transcribes and summarizes video content using advanced AI models. This tool uses OpenAI's Whisper for speech recognition and Hugging Face's T5 transformer model for text summarization, all wrapped in a user-friendly PyQt5 interface.
Features

Video Upload: Easily select video files from your computer
Automatic Transcription: Converts speech to text using Whisper AI
Smart Summarization: Generates concise summaries using T5 transformer
Copy & Save: Options to copy summaries to clipboard or save to file
Progress Tracking: Visual progress bar shows processing status
Modern UI: Clean and intuitive interface with dark mode design

Technologies Used

Python 3.x: Core programming language
PyQt5: GUI framework
OpenAI Whisper: State-of-the-art speech recognition model
Hugging Face Transformers: NLP models for text summarization
MoviePy: Video processing library
QtAwesome: Icon pack for UI elements

Installation

Clone this repository:

Copygit clone https://github.com/mutassimalzeem/ai-video-summarizer.git
cd ai-video-summarizer

Install the required packages:

Copypip install PyQt5 qtawesome openai-whisper transformers moviepy torch

Run the application:

Copypython video_summarizer.py
Usage

Launch the application
Click the "Upload Video" button to select a video file
Wait for the AI to process the video (this may take several minutes depending on video length)
View the generated summary in the text area
Use the "Copy Summary" button to copy to clipboard, or "Save Summary" to save as a text file

System Requirements

Python 3.8 or higher
8GB+ RAM recommended
NVIDIA GPU with CUDA support (optional, for faster processing)
500MB+ disk space for models

Project Structure
Copyai-video-summarizer/
├── video_summarizer.py      # Main application file
├── requirements.txt         # Required Python packages
├── README.md                # This file
└── temp/                    # Temporary folder for audio processing
Future Improvements

 Add support for multiple languages
 Implement batch processing for multiple videos
 Add option to customize summary length
 Create export options in different formats (PDF, DOCX)
 Implement more sophisticated summarization techniques

License
MIT License - See LICENSE file for details
Acknowledgements

OpenAI Whisper for the speech recognition model
Hugging Face for the T5 summarization model
PyQt5 for the application framework

Contributors

Mutassim Al Shahriar Zeem - Initial work and maintenance

Contact
Please open an issue on this repository or contact mutassimalshahriar@gmail.com for questions, suggestions, or collaborations.
