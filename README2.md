# AI Video Summarizer

![Screenshot 2025-03-16 120558](https://github.com/user-attachments/assets/cb986436-7b1f-4dfa-8c2d-4d02c7612794)


https://github.com/user-attachments/assets/b97b9627-ac9f-4b2a-964f-f399253e28e1

## Description

AI Video Summarizer is a desktop application that automatically transcribes and summarizes video content using advanced AI models. This tool uses OpenAI's Whisper for speech recognition and Hugging Face's T5 transformer model for text summarization, all wrapped in a user-friendly PyQt5 interface.

## Features



- **Video Upload**: Easily select video files from your computer
- **Automatic Transcription**: Converts speech to text using Whisper AI
- **Smart Summarization**: Generates concise summaries using T5 transformer
- **Copy & Save**: Options to copy summaries to clipboard or save to file
- **Progress Tracking**: Visual progress bar shows processing status
- **Modern UI**: Clean and intuitive interface with dark mode design

## Technologies Used

- **Python 3.x**: Core programming language
- **PyQt5**: GUI framework
- **OpenAI Whisper**: State-of-the-art speech recognition model
- **Hugging Face Transformers**: NLP models for text summarization
- **MoviePy**: Video processing library
- **QtAwesome**: Icon pack for UI elements

## Installation

1. Clone this repository:
```
git clone https://github.com/mutassimalzeem/ai-video-summarizer.git
cd ai-video-summarizer
```

2. Install the required packages:
```
pip install PyQt5 qtawesome openai-whisper transformers moviepy torch
```

3. Run the application:
```
python ai-video-summarizer.py
```

## Usage

1. Launch the application
2. Click the "Upload Video" button to select a video file
3. Wait for the AI to process the video (this may take several minutes depending on video length)
4. View the generated summary in the text area
5. Use the "Copy Summary" button to copy to clipboard, or "Save Summary" to save as a text file

## System Requirements

- Python 3.8 or higher
- 8GB+ RAM recommended
- NVIDIA GPU with CUDA support (optional, for faster processing)
- 500MB+ disk space for models

## Project Structure

```
ai-video-summarizer/
├── video_summarizer.py      # Main application file
├── requirements.txt         # Required Python packages
├── README.md                # This file
└── temp/                    # Temporary folder for audio processing
```

## Future Improvements

- [ ] Add support for multiple languages
- [ ] Implement batch processing for multiple videos
- [ ] Add option to customize summary length
- [ ] Create export options in different formats (PDF, DOCX)
- [ ] Implement more sophisticated summarization techniques

## License

MIT License - See LICENSE file for details

## Acknowledgements

- OpenAI Whisper for the speech recognition model
- Hugging Face for the T5 summarization model
- PyQt5 for the application framework

## Contributors

- Mutassim Al Shahriar Zeem - Initial work and maintenance

## Contact

For questions, suggestions, or collaborations, please open an issue on this repository or contact [mutassimalshahriar@gmail.com](mutassimalshahriar@gmail.com).
