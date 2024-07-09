import streamlit as st
import assemblyai as aai

# Set your AssemblyAI API key
aai.settings.api_key = "API_KEY"

# Streamlit app title
st.title("Audio Transcriber")

# File uploader
uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "m4a"])

# Transcribe button
if uploaded_file is not None:
    if st.button("Transcribe"):
        # Transcribe the audio file
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(uploaded_file)

        # Display the transcription
        if transcript.status == aai.TranscriptStatus.error:
            st.error(transcript.error)
        else:
            st.success("Transcription complete!")
            st.write(transcript.text)
