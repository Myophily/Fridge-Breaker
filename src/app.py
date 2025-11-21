"""Main Streamlit application for Fridge Breaker"""

import streamlit as st
from gemini_client import GeminiClient
from ui_components import (
    render_header,
    render_ingredient_inputs,
    render_seasonings_input,
    render_tools_inputs,
    render_preferences,
    render_footer,
    create_recipe_prompt
)


def main():
    """Main application entry point"""
    # Page configuration
    st.set_page_config(page_title="Fridge Breaker")

    # Initialize Gemini client
    gemini_api_key = st.secrets["GEMINI_API_KEY"]
    client = GeminiClient(gemini_api_key)

    # Render UI sections
    render_header()

    # Input sections
    ingredients_text, ingredients_images = render_ingredient_inputs()
    seasonings = render_seasonings_input()
    tools_text, tools_images = render_tools_inputs()
    difficulty, cuisine, diet, health = render_preferences()

    # Recipe generation button
    col5, col6 = st.columns([3, 1])

    with col5:
        if st.button('레시피 받기'):
            # Process images
            ingredients_from_images = client.process_uploaded_images(
                ingredients_images,
                "이 이미지에서 보이는 식재료들을 쉼표로 구분하여 나열해주세요."
            )
            tools_from_images = client.process_uploaded_images(
                tools_images,
                "이 이미지에서 보이는 조리도구들을 쉼표로 구분하여 나열해주세요."
            )

            # Combine inputs
            all_ingredients = f"{ingredients_text}, {ingredients_from_images}".strip(', ')
            all_tools = f"{tools_text}, {tools_from_images}".strip(', ')

            # Generate recipe
            prompt = create_recipe_prompt(
                all_ingredients,
                seasonings,
                all_tools,
                difficulty,
                cuisine,
                diet,
                health
            )

            with st.spinner('레시피 생성 중...'):
                recipe = client.generate_response(prompt)

            st.subheader('Gemini를 통한 추천 레시피:')
            st.markdown(recipe)

    with col6:
        st.markdown('Powered By GEMINI')

    # Footer
    render_footer()


if __name__ == "__main__":
    main()
