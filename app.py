from flask import Flask, request, render_template, redirect, url_for
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from transformers import pipeline

app = Flask(__name__)

# Load the Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="t5-small")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    video_url = request.form.get("video_url")
    
    # Extract video ID from the URL
    try:
        video_id = video_url.split("v=")[1]
    except IndexError:
        return render_template("result.html", transcript="Invalid YouTube URL.", summary="")

    # Fetch the transcript
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([item['text'] for item in transcript])
    except TranscriptsDisabled:
        return render_template("result.html", transcript="No captions available for this video.", summary="")

    # Summarize the transcript
    try:
        summary = summarizer(transcript_text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    except Exception as e:
        summary = f"An error occurred during summarization: {str(e)}"

    return render_template("result.html", transcript=transcript_text, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
