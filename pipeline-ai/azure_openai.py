# import requests

# # Ganti dengan kunci API dan endpoint Anda
# api_key = '224746b6ce8e4ddeac4a2a9442db5466'
# endpoint = 'https://danie-m2lgughl-westeurope.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2024-08-01-preview'

# # Contoh payload untuk permintaan
# payload = {
#     "messages": [
#         {"role": "user", "content": "Hello, how can I use Azure OpenAI?"}
#     ]
# }

# # Pengaturan header untuk permintaan
# headers = {
#     "Content-Type": "application/json",
#     "api-key": api_key  # Pastikan menggunakan 'api-key', bukan 'Bearer'
# }

# # Kirim permintaan ke API
# response = requests.post(endpoint, json=payload, headers=headers)

# # Tampilkan hasil
# print(response.json())

import requests

# Ganti dengan kunci API dan endpoint Anda
api_key = '224746b6ce8e4ddeac4a2a9442db5466'
endpoint = 'https://danie-m2lgughl-westeurope.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2024-08-01-preview'

# Pengaturan header untuk permintaan
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

# Inisialisasi pesan
conversation = []

# Mulai percakapan
print("Mulai percakapan dengan model (ketik 'exit' untuk keluar).")

while True:
    # Ambil input dari pengguna
    user_input = input("Anda: ")
    
    # Jika pengguna mengetik 'exit', hentikan percakapan
    if user_input.lower() == "exit":
        print("Percakapan selesai.")
        break
    
    # Tambahkan input pengguna ke percakapan
    conversation.append({"role": "user", "content": user_input})
    
    # Siapkan payload untuk API
    payload = {
        "messages": conversation
    }
    
    # Kirim permintaan ke API
    response = requests.post(endpoint, json=payload, headers=headers)
    result = response.json()

    # Dapatkan respons dari model
    assistant_message = result['choices'][0]['message']['content']
    
    # Tampilkan respons model
    print(f"AI: {assistant_message}")
    
    # Tambahkan respons model ke percakapan
    conversation.append({"role": "assistant", "content": assistant_message})
