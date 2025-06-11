import ollama

paragraph = """
During the pre-Inca period, people lived in clans, which formed great tribes,
some allied with each other to form powerful confederations, as the Confederation of Quito.
But none of these confederations could resist the formidable momentum of the Tawantinsuyu.
The invasion of the Incas in the 16th century was very painful and bloody.
However, once occupied by the Quito hosts of Huayna Capac (1523–1525),
the Incas developed an extensive administration and began the colonization of the region.
The Pre-Columbian era can be divided up into four eras: the Pre-ceramic Period,
the Formative Period, the Period of Regional Development and the Period of Integration and the Arrival of the Incas.
"""


prompt = f"""
Give me the 5 more important words from the following paragraph:

{paragraph}
"""


def main():
    client = ollama.Client()

    resp = client.generate(
        model="llama3.2",
        prompt=prompt,
    )

    print("Response:", resp.response)


main()
