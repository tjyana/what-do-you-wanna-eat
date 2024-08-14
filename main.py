import streamlit as st
from utils.functions import suggest_food, image_generator
import random

titles = ['You should eat...', 'How about...', 'I recommend...', 'Try this!', 'Why not...',
          'Have you had...', 'You might like...', 'Consider...', 'What about...']
random_title = random.choice(titles)

def main():
    # Title
    st.sidebar.title("What do you wanna eat?")
    st.sidebar.write("Please tell me your preferences:")

    # Input fields
    favorite_foods = st.sidebar.text_input("Favorite foods")
    favorite_flavors = st.sidebar.text_input("Favorite flavors or cuisines")
    dislikes = st.sidebar.text_input("Want to avoid (dislikes, allergies, recent meals)")
    others = st.sidebar.text_input("Other considerations (optional)")

    # Submit button
    if st.sidebar.button("Submit"):
        # Process the inputs
        st.session_state.favorite_foods = favorite_foods
        st.session_state.favorite_flavors = favorite_flavors
        st.session_state.dislikes = dislikes
        st.session_state.others = others

        st.header(random_title)
        print('generating food...')
        output = suggest_food(favorite_foods, favorite_flavors, dislikes, others)

        food = output.split("$PL!T")[0]
        analysis = output.split("$PL!T")[-1]
        st.header(food)

        try:
            url = image_generator(output)
            # st.image('https://bytedance-sdxl-lightning.hf.space/file=/tmp/gradio/eafcc0db1b589bdbce8ba19c5968a6cc74df6504/image.webp', use_column_width=True)
            st.image(url, use_column_width=True)
        except Exception as e:
            st.warning("[Could not generate image. Please imagine something really really good!]")
            print(f"Error generating image: {e}")

        st.write(analysis)



if __name__ == "__main__":
    main()
