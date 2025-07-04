from openai import OpenAI

openai = OpenAI(
    api_key="SrlxY18iY2rKmZnQ3dtkHZIzVW9tN4dH",
    base_url="https://api.deepinfra.com/v1/openai"
)

stream = False

def ask_english_bot():
    print("🎓 English Chatbot (gõ 'e' để thoát)")
    while True:
        user_input = input("👤 Bạn: ")
        if user_input.lower() == "e":
            print("Goodbye!")
            break

        chat_completion = openai.chat.completions.create(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            messages=[
                {"role": "system", "content": "You are a friendly English teacher helping Vietnamese high school students."},
                {"role": "user", "content": user_input}
            ],
            stream=stream,
        )

        if stream:
            print("🤖 Bot: ", end="")
            for event in chat_completion:
                if not event.choices[0].finish_reason:
                    print(event.choices[0].delta.content, end="", flush=True)
            print()
        else:
            message = chat_completion.choices[0].message.content
            print(f"🤖 Bot: {message}")
            print("––––––––––––––––––––––––––––––––––––")

ask_english_bot()
