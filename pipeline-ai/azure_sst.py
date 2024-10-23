import azure.cognitiveservices.speech as speechsdk

# Key and endpoint
speech_key = "4d210f9e547840a7a9cc0a47784a3035"  # Ganti dengan kunci Anda
service_region = "southeastasia"  # Ganti dengan wilayah Anda

# Initiate the config 
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Use default microphone as audio input
audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

# Create a recognizer
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

print("Speak into your microphone.")

# Start speech recognition
result = speech_recognizer.recognize_once_async().get()

# Check the result
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print(f"Recognized: {result.text}")
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech was recognized.")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print(f"Speech recognition canceled: {cancellation_details.reason}")
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print(f"Error details: {cancellation_details.error_details}")
