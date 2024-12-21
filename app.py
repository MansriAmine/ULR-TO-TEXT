from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

# Function to extract transcript from YouTube
def get_transcript(video_url):
    # Extract the video ID from the URL
    video_id = video_url.split("v=")[1]
    try:
        # Fetch the transcript using youtube-transcript-api
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        return None

# Route for the main page with the form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the YouTube URL submission and return the transcript
@app.route('/submit', methods=['POST'])
def submit_video():
    # Get the YouTube video URL from the form
    video_url = request.form['video_url']

    # Get the transcript
    transcript = get_transcript(video_url)

    if transcript:
        # Format transcript as text (can also return SRT or JSON format)
        transcript_text = " ".join([item['text'] for item in transcript])
        return render_template('result.html', transcript=transcript_text)
    else:
        return render_template('result.html', transcript="Transcript not available for this video.")

if __name__ == '__main__':
    app.run(debug=True)
