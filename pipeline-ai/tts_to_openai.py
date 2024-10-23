import requests
import azure.cognitiveservices.speech as speechsdk

# Konfigurasi API OpenAI
api_key = '224746b6ce8e4ddeac4a2a9442db5466'
endpoint = 'https://danie-m2lgughl-westeurope.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2024-08-01-preview'

# Konfigurasi header untuk OpenAI API
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

# Konfigurasi Azure Speech Service untuk Text-to-Speech
speech_key = "4d210f9e547840a7a9cc0a47784a3035"
service_region = "southeastasia"

# Inisialisasi konfigurasi Azure Speech
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.speech_synthesis_voice_name = "id-ID-ArdiNeural"  # Suara bahasa Indonesia
audio_config = speechsdk.audio.AudioOutputConfig(filename="output.wav")
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

while True:
    # Input percakapan dari user
    user_input = input("Masukkan pertanyaan atau pernyataan (ketik 'exit' untuk keluar): ")
    if user_input.lower() == 'exit':
        break

    # Siapkan payload untuk OpenAI API
    payload = {
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    # Kirim permintaan ke API OpenAI
    response = requests.post(endpoint, json=payload, headers=headers)
    result = response.json()

    # Ambil teks dari respons OpenAI
    if 'choices' in result and len(result['choices']) > 0:
        openai_output = result['choices'][0]['message']['content']
        print(f"Output dari OpenAI: {openai_output}")

        # Gunakan teks dari OpenAI sebagai input untuk Azure TTS
        if openai_output:
            result = speech_synthesizer.speak_text_async(openai_output).get()

            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                print("Suara telah disintesis dan disimpan ke file output.wav dengan sukses.")
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = result.cancellation_details
                print(f"Sintesis suara dibatalkan: {cancellation_details.reason}")
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print(f"Detail kesalahan: {cancellation_details.error_details}")
    else:
        print("Tidak ada output dari OpenAI.")
