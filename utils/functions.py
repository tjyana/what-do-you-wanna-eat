import streamlit as st
import google.generativeai as genai
from openai import OpenAI


api_key = st.secrets['OPENAI_API_KEY']


def suggest_food(favorite_foods, favorite_flavors, dislikes, others):
    '''
    Generate a food suggestion based on the user's input.
    Load the model, generate the content, and return the response.
    '''

    model = genai.GenerativeModel('gemini-1.5-flash')

    with st.spinner('Thinking of what to eat...'):
        response = model.generate_content(f"""
        Favorite foods: ```{favorite_foods}```
        Favorite flavors and cuisines: ```{favorite_flavors}```
        Other considerations: ```{others}```
        Do not suggest: ``` {dislikes}```

        Given the above information, please analyze this person's favorite foods, flavors, and cuisines.
        Based on this, provide a recommendation for a meal that they would enjoy.

        If possible, please try to extrapolate flavor profiles of their favorite dishes,
        and recommend foods with similar flavors or ingredients from other cuisines.

        eg. If they say their favorite dish is spaghetti:
        -> similar flavors (savory, umami, tomato, garlic, basil, oregano)
        -> similar ingredients (pasta, tomato sauce, ground meat, garlic, basil, oregano)
        -> recommend a dish with similar flavors or ingredients from another cuisine (eg. lasagna, moussaka, shakshuka)

        If you're going to suggest a non-Western food, please try to be specific as possible and provide
        the name of the recipe in that language.
        Please avoid terms like "Asian" or "Indian" or generic terms like "curry" or "stir-fry" as they are too broad.
        If inputs don't make sense, please consider that it may be a non-English word spelled out in English.

        Output format:

        [Name of the dish]
        [Short summary of what's in the dish ~20 words]

        $PL!T

        Analysis: [Analysis of the favorite foods, flavors, and cuisines]



        Example output format:

        Korean Bulgogi Tacos    \n
        Thinly sliced marinated beef, grilled and served in warm tortillas with kimchi and gochujang mayo.  \n

        $PL!T   \n

        Analysis: This person enjoys classic American comfort food with a focus on hearty, savory flavors and a preference for spicy dishes. Burgers, pizza, and nachos all feature bold flavor profiles and often incorporate spicy elements like jalapeños or chili peppers. Korean Bulgogi Tacos offer a similar combination of savory, smoky, and spicy flavors with the umami richness of beef and the spicy kick of gochujang.

        """)

    answer = response.text

    return answer


def image_generator(answer):
    '''
    Generate an image based on the user's input.
    Load the model, generate the image (spinner while loading), and return the image URL.
    '''

    client = OpenAI()

    with st.spinner('Generating image...'):
        response = client.images.generate(
        model="dall-e-3",
        prompt=answer,
        size="1024x1024",
        quality="standard",
        n=1,
        )

    image_url = response.data[0].url

    return image_url
