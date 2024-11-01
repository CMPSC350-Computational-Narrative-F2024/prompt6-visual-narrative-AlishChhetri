import os
import requests
from dotenv import dotenv_values

# Load API configuration
CONFIG = dotenv_values(".env")
OPEN_AI_KEY = CONFIG["KEY"] or os.environ["OPEN_AI_KEY"]


def create_output_dirs():
    """Creates output directory for images."""
    image_dir = "img"
    os.makedirs(image_dir, exist_ok=True)
    return image_dir


def generate_image(prompt, chapter_name, image_dir):
    """Generates a cartoony-style image for a comic panel using DALL-E."""
    image_filename = os.path.join(
        image_dir, f"{chapter_name.replace(' ', '_').lower()}_image.png"
    )

    if os.path.exists(image_filename):
        print(f"Using cached image for '{chapter_name}'.")
        return image_filename

    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Authorization": f"Bearer {OPEN_AI_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "dall-e-3",
            "prompt": f"{prompt} in a cartoony illustration style, similar to the Magic Treehouse series.",
            "n": 1,
            "size": "1024x1024",
        },
    )
    if response.status_code == 200:
        image_url = response.json()["data"][0]["url"]
        with open(image_filename, "wb") as f:
            f.write(requests.get(image_url).content)
        print(f"Generated new image for '{chapter_name}'.")
        return image_filename
    else:
        raise Exception(
            f"Image generation failed: {response.status_code} {response.text}"
        )


def create_markdown(book_title, chapters):
    """Generates a markdown file for the comic narrative with images only."""
    markdown_content = f"# {book_title}\n\n"

    # Add each panel's image only
    for chapter in chapters:
        markdown_content += f"![{chapter['title']} Image](../src/img/{os.path.basename(chapter['image'])})\n\n"
        markdown_content += "---\n"

    output_filename = "../writing/comic.md"
    with open(output_filename, "w") as md_file:
        md_file.write(markdown_content)

    print(f"Markdown file generated: {output_filename}")
    return output_filename


def create_comic_book():
    """Creates comic panels and generates a markdown narrative with images only."""
    book_title = "History Comes Alive"
    image_dir = create_output_dirs()

    # Pre-defined prompts for each panel with images only
    panel_prompts = [
        {
            "title": "Bored in Class",
            "image_prompt": "A child yawning in a classroom with a history book on the desk, in a cartoony style.",
        },
        {
            "title": "Time Travel Begins",
            "image_prompt": "A swirling colorful portal opening near the child in the classroom.",
        },
        {
            "title": "Ancient Egypt",
            "image_prompt": "The child looking amazed while standing in ancient Egypt with a pyramid in the background, cartoon style.",
        },
        {
            "title": "Medieval Castle",
            "image_prompt": "A child watching knights in armor near a castle, illustrated in a cartoony style.",
        },
        {
            "title": "Renaissance Art",
            "image_prompt": "A child observing an artist painting in a Renaissance studio, in a cartoony illustration style.",
        },
        {
            "title": "Industrial Revolution",
            "image_prompt": "A child looking at a city with factories and smokestacks, cartoony style.",
        },
        {
            "title": "Early Flight",
            "image_prompt": "A child watching an old-fashioned airplane take off, with excitement, in a cartoon style.",
        },
        {
            "title": "Historical Scene",
            "image_prompt": "A child observing a scene with soldiers and vehicles from a past era, illustrated in a cartoony style.",
        },
        {
            "title": "Historic March",
            "image_prompt": "A child in a crowd, observing people holding signs and walking together, in a cartoony illustration style.",
        },
        {
            "title": "Space Exploration",
            "image_prompt": "A child looking up at an astronaut on the moon, with the Earth in the background, illustrated in a cartoony style.",
        },
        {
            "title": "Back to Class",
            "image_prompt": "The child reappearing in the classroom, looking excited, with the history book open on the desk.",
        },
        {
            "title": "History is Amazing!",
            "image_prompt": "A child eagerly talking to friends in a classroom setting, in a cartoon style.",
        },
    ]

    chapters = []
    for prompt in panel_prompts:
        # Generate image for each chapter
        panel_image = generate_image(prompt["image_prompt"], prompt["title"], image_dir)
        chapters.append({"title": prompt["title"], "image": panel_image})

    create_markdown(book_title, chapters)

    with open("img/image_explanation", "w") as img_exp_file:
        img_exp_file.write(
            "Explanation of Panel 1: Kid yawning in class saying 'History is boring.'"
        )


if __name__ == "__main__":
    create_comic_book()
