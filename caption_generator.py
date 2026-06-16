from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_caption(topic):

    prompt = f"Meme about {topic}:"

    result = generator(
        prompt,
        max_length=15,
        num_return_sequences=1,
        truncation=True
    )

    caption = result[0]["generated_text"]

    return caption