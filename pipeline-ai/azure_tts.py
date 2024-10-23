# import os
# import azure.cognitiveservices.speech as speechsdk

# # Key and endpoint
# speech_key = "4d210f9e547840a7a9cc0a47784a3035"
# service_region = "southeastasia"

# # Initiate the config 
# speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# # output
# speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"

# audio_config = speechsdk.audio.AudioOutputConfig(filename="output.wav")
# speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# text = "Hello, this is a test of Azure Speech Service."

# result = speech_synthesizer.speak_text_async(text).get()

# if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#     print("Speech synthesized and saved to output.wav file successfully.")
# elif result.reason == speechsdk.ResultReason.Canceled:
#     cancellation_details = result.cancellation_details
#     print(f"Speech synthesis canceled: {cancellation_details.reason}")
#     if cancellation_details.reason == speechsdk.CancellationReason.Error:
#         print(f"Error details: {cancellation_details.error_details}")
 
import os
import azure.cognitiveservices.speech as speechsdk

# Key and endpoint
speech_key = "4d210f9e547840a7a9cc0a47784a3035"
service_region = "southeastasia"

# Initiate the config 
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Output
# Ganti dengan suara bahasa Indonesia
speech_config.speech_synthesis_voice_name = "id-ID-ArdiNeural"  # Contoh suara bahasa Indonesia

audio_config = speechsdk.audio.AudioOutputConfig(filename="output.wav")
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

text = "Nama gue Daniel. Mobilku banyak, harta berlimpah"

result = speech_synthesizer.speak_text_async(text).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Suara telah disintesis dan disimpan ke file output.wav dengan sukses.")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print(f"Sintesis suara dibatalkan: {cancellation_details.reason}")
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print(f"Detail kesalahan: {cancellation_details.error_details}")
