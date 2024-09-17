# Subtitles Generator Using Python

This is a small effort to create a video subtitles generator using Python's built-in libraries and Google's Web Speech API. The project processes audio or video files, converts the speech into text, and outputs the results in SRT (SubRip Subtitle) format.

## Features

- **Speech Recognition**: Uses Google Web Speech API to transcribe speech from media files.
- **SRT Subtitle Generation**: Automatically generates subtitles with timestamps in SRT format.
- **File Handling**: Writes the recognized speech to a notepad document in SRT form for easy use in video editing.

## Supported Speech Recognition APIs

While this project uses **Google Web Speech API**, Python supports the following additional APIs for speech recognition:

- Microsoft Bing Speech
- Google Cloud Speech (requires `google-cloud-speech` package)
- Houndify by Sound Hound
- IBM Speech to Text
- CMU Sphinx (requires installing `Pocket Sphinx`)
- Wit.ai

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x
- PyDub (`pip install pydub`)
- MoviePy (`pip install moviepy`)
- SpeechRecognition (`pip install SpeechRecognition`)
- FFMPEG (for processing media files)

## Contributing

Feel free to fork this repository and contribute improvements or new features. Pull requests are welcome!

## Acknowledgements

- Google's Web Speech API for speech recognition functionality.
- Python's built-in libraries for handling files and processing media.
