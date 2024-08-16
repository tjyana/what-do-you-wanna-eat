import streamlit as st
from utils.functions import suggest_food, image_generator
import random


def main():
    '''
    Main function for the Streamlit app.
    Takes user inputs and displays the food suggestion.
    (split into two functions for better organization if app gets more complex)
    '''

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

        # Display the header
        titles = ['You should eat...', 'How about...', 'I recommend...', 'Try this!', 'Why not...',
          'Have you had...', 'You might like...', 'Consider...', 'What about...']
        random_title = random.choice(titles)
        st.header(random_title)

        # Get the food suggestion
        output = suggest_food(favorite_foods, favorite_flavors, dislikes, others)
        # Split the output into food and analysis
        food = output.split("$PL!T")[0]
        analysis = output.split("$PL!T")[-1]

        # Display Food Suggestion
        st.header(food)

        # Display Image
        try:
            url = image_generator(food)
            st.image(url, use_column_width=True)
        except Exception as e:
            st.warning("[Could not generate image. Please imagine something really really good!]")
            print(f"Error generating image: {e}")

        # Display Analysis
        st.write(analysis)



if __name__ == "__main__":
    main()
