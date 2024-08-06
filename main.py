

def main():
    # Title
    st.sidebar.title("Food Recommender")
    st.sidebar.write("Hello! Please tell me your preferences:")

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

        output = suggest_food(favorite_foods, favorite_flavors, dislikes, others)


        # output = suggest_food(favorite_foods, favorite_flavors, dislikes, others, last_output)


        url = image_generator(output)

        # add func to keep last output from showing
        # st.session_state.last_output = output.split("\n")[-2]

        process_inputs(output, url)



def process_inputs(input1, url):
    # Function to display the final output
    # Process the inputs here
    st.write(" ", input1)
    st.image(url, use_column_width=True)


if __name__ == "__main__":
    main()
