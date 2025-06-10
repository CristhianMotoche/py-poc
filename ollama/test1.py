import ollama


def main():
    client = ollama.Client()

    resp = client.list()
    print("Available models:")
    for model in resp['models']:
        print(' -', model.model)

    chatResp = client.chat(
        model="llama3.2",
        messages=[
            { "role": "assistant",
              "content": "Give me a list of 5 progressive metal bands."
            },
        ]
    )

    print("Chat response:", chatResp.message)
    print("Chat response content:", chatResp.message.content)


main()
