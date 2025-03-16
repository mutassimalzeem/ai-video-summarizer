import sys, threading, os, whisper
import qtawesome as qta
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QTextEdit, QVBoxLayout,
    QFileDialog, QProgressBar
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, pyqtSignal, QObject

from transformers import pipeline
import moviepy.editor as mp


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.
    """
    progress = pyqtSignal(int)
    result = pyqtSignal(str)
    error = pyqtSignal(str)


class VideoSummarizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.model = whisper.load_model("medium")
        self.summarizer = pipeline("summarization", model="t5-small")
        self.signals = WorkerSignals()
        self.signals.progress.connect(self.update_progress)
        self.signals.result.connect(self.update_result)
        self.signals.error.connect(self.show_error)

    def initUI(self):
        self.setWindowTitle("AI Video Summarizer")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #2c3e50; color: white;")

        font = QFont("Arial", 12)

        self.label = QLabel("Select a video file:", self)
        self.label.setFont(font)

        self.uploadBtn = QPushButton(qta.icon("fa5s.upload"), " Upload Video", self)
        self.uploadBtn.setStyleSheet("background-color: #16a085; color: white; padding: 8px; border-radius: 5px;")
        self.uploadBtn.clicked.connect(self.load_video)

        self.progressBar = QProgressBar(self)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setStyleSheet("QProgressBar::chunk { background-color: #27ae60; }")
        self.progressBar.setValue(0)

        self.resultText = QTextEdit(self)
        self.resultText.setReadOnly(True)
        self.resultText.setStyleSheet("background-color: #34495e; color: white; padding: 5px;")

        self.copyBtn = QPushButton(qta.icon("fa5s.copy"), " Copy Summary", self)
        self.copyBtn.setStyleSheet("background-color: #2980b9; color: white; padding: 8px; border-radius: 5px;")
        self.copyBtn.clicked.connect(self.copy_summary)

        self.saveBtn = QPushButton(qta.icon("fa5s.save"), " Save Summary", self)
        self.saveBtn.setStyleSheet("background-color: #e67e22; color: white; padding: 8px; border-radius: 5px;")
        self.saveBtn.clicked.connect(self.save_summary)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.uploadBtn)
        layout.addWidget(self.progressBar)
        layout.addWidget(self.resultText)
        layout.addWidget(self.copyBtn)
        layout.addWidget(self.saveBtn)
        self.setLayout(layout)

    def load_video(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Videos (*.mp4 *.avi *.mov)", options=options)
        if filePath:
            self.process_video(filePath)

    def process_video(self, filePath):
        self.signals.progress.emit(10)
        self.resultText.setPlainText("Processing video... Please wait...")
        # Set buttons to disabled state during processing
        self.uploadBtn.setEnabled(False)
        self.copyBtn.setEnabled(False)
        self.saveBtn.setEnabled(False)
        
        # Create and start the worker thread
        thread = threading.Thread(
            target=self.transcribe_and_summarize, 
            args=(filePath, self.signals),
            daemon=True
        )
        thread.start()

    def transcribe_and_summarize(self, filePath, signals):
        try:
            signals.progress.emit(20)
            
            # Create a temp folder in the current directory if it doesn't exist
            temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
            os.makedirs(temp_dir, exist_ok=True)
            temp_audio_path = os.path.join(temp_dir, "temp_audio.wav")
            
            # Extract audio
            clip = mp.VideoFileClip(filePath)
            clip.audio.write_audiofile(temp_audio_path, verbose=False, logger=None)
            
            signals.progress.emit(50)
            
            # Transcribe with Whisper
            transcription = self.model.transcribe(temp_audio_path)["text"]
            
            signals.progress.emit(70)
            
            # Handle long transcriptions with chunking
            if len(transcription) > 1000:
                chunks = [transcription[i:i+1000] for i in range(0, len(transcription), 1000)]
                summaries = []
                
                for i, chunk in enumerate(chunks[:3]):  # Limit to first 3 chunks to avoid very long processing
                    summary_chunk = self.summarizer(chunk, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
                    summaries.append(summary_chunk)
                
                if len(chunks) > 3:
                    final_summary = "Summary (first part of video):\n\n" + " ".join(summaries)
                else:
                    final_summary = "Full Video Summary:\n\n" + " ".join(summaries)
            else:
                final_summary = self.summarizer(transcription, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
            
            signals.progress.emit(100)
            signals.result.emit(final_summary)
            
            # Clean up
            try:
                if os.path.exists(temp_audio_path):
                    os.remove(temp_audio_path)
            except:
                pass  # Silently fail if cleanup errors
                
        except Exception as e:
            signals.error.emit(f"Error: {str(e)}")

    def update_progress(self, value):
        self.progressBar.setValue(value)
        
    def update_result(self, summary):
        self.resultText.setPlainText(summary)
        # Re-enable buttons once processing is complete
        self.uploadBtn.setEnabled(True)
        self.copyBtn.setEnabled(True)
        self.saveBtn.setEnabled(True)
        
    def show_error(self, error_message):
        self.resultText.setPlainText(error_message)
        self.progressBar.setValue(0)
        # Re-enable buttons on error
        self.uploadBtn.setEnabled(True)
        self.copyBtn.setEnabled(True)
        self.saveBtn.setEnabled(True)

    def copy_summary(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.resultText.toPlainText())

    def save_summary(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Summary", "summary.txt", "Text Files (*.txt)")
        if filePath:
            with open(filePath, "w", encoding="utf-8") as f:
                f.write(self.resultText.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoSummarizerApp()
    window.show()
    sys.exit(app.exec_())