# YouTube Transcript Fetcher

This project is a web application that fetches the transcript of a YouTube video and provides a summary of the transcript using a machine learning model.

## Features

- Fetches the transcript of a YouTube video.
- Summarizes the transcript using the Hugging Face `t5-small` model.
- Simple and user-friendly interface.

![Alt text](draw.png)

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter the URL of the YouTube video you want to fetch the transcript for and click "Get Transcript".
![Alt text](html_YoutubeTranscriptAPI.png)
this is the fetched transcript
![Alt text](result.png)
this is the summarized transcript
![Alt text](summary.png)

## Project Structure


- app.py: The main Flask application file.
- templates: Directory containing HTML templates.
  - index.html: The main page where users can enter the YouTube video URL.
  - result.html: The page that displays the fetched transcript and summary.
- static: Directory containing CSS files.
  - index.css: Styles for the main page.
  - result.css: Styles for the result page.
  
## Dependencies

- Flask
- youtube_transcript_api
- transformers


