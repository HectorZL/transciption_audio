# Audio-to-Text Transcription with Python

This Python script uses the "whisper" package to transcribe an audio file to text.

## Features

- Transcribes audio files to text
- Supports various audio file formats (e.g. mp3, wav, m4a)
- Utilizes a pre-trained model to transcribe audio
- Saves transcribed text to a text file

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running: `pip install -r requirements.txt`

## Usage

1. Place an audio file to be transcribed in the root directory of this repository.
2. In the terminal, navigate to the root directory of this repository.
3. Run the following command: 
   `python transcribe_audio.py filename.extension`
4. Replace "filename.extension" with the name of the audio file to be transcribed (e.g. example.mp3, recording.wav, interview.m4a)
5. After running the script, a text file named "transcription.txt" will be created in the root directory containing the transcribed text.

## Credits

This project was created with the "whisper" package. 

## License

This project is licensed under the GNU GPL v3 License. You are free to use, modify, and distribute this software as long as any changes to the software are made available under the same license. See the LICENSE file for details.
