# what-do-you-wanna-eat

When you need to decide what to eat with another person

Short term plans:
- load image last
- separate out allergies/dietary restrictions
- refactor main()

Other functionalities being considered:
- more input fields for two people? one player mode and two player mode?

- after food is suggested
  -> output recipe option? hell yea
  -> 'Why did we suggest this?' in expandable thing. (show the analysis portion)
    - probably high priority, so ppl can see the justification

- generate again option. keep last denied output in mind. feedback gathering?




The FULL ML app idea:
- takes user inputs, gathers feedback on the output
  -> that data is used to train a ML model that predicts foods that the user would like
  -> other data is incorporated: time data (time of day, day of week, month etc), emotional? (moods), idk what else
    -> pipeline to carry that data and train the model etc is required.
- RAG stuff for all the prompt? not sure how that works. BERT?






Example output:
Spicy Garlic Chicken with Creamy Coconut Rice
Spicy Garlic Chicken with Creamy Coconut Rice: A flavorful dish with tender chicken marinated in a spicy garlic sauce, served over aromatic coconut rice.

Flavor Profile: This dish features a combination of savory, spicy, and creamy flavors. The garlic and chili peppers provide a strong, pungent flavor, while the coconut milk adds a rich, creamy element.

Similar Flavors and Ingredients from other cuisines:

Korean: 닭갈비 (Dakgalbi): A spicy stir-fry dish with chicken, vegetables, and gochujang (Korean chili paste). The fiery gochujang sauce creates a similar flavor profile to the spicy garlic marinade.
Thai: ไก่ผัดพริกไทยดำ (Gai Pad Prik Thai Dam): A Thai stir-fry dish with chicken, black peppercorns, and garlic. This dish features the same core ingredients as the Spicy Garlic Chicken, with the addition of black pepper for a slightly different flavor.
