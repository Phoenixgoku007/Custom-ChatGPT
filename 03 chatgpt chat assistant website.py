'''For pro guys who can write their own customisable codes on python'''

import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a senior backend developer in django and have great expertise in teaching it to junior developers and interns"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Pro Coder")

demo.launch(share=True)