"""UI components for Fridge Breaker app"""

import streamlit as st


def render_header():
    """Render the app header"""
    st.title('Fridge Breaker (냉장고 털어먹기)')
    st.write('냉장고 속 재료로 만들 수 있는 요리를 추천받고 레시피를 확인하세요.')
    st.write('집에 있는 재료와 조리도구를 입력하거나 사진을 업로드하세요.')


def render_ingredient_inputs():
    """Render ingredient input section"""
    col1, col2 = st.columns(2)

    with col1:
        placeholder_text = """Ex)
감자
파
..."""
        ingredients_text = st.text_area(
            '재료를 입력하세요 (줄바꿈으로 구분):',
            placeholder=placeholder_text,
            height=100
        )

    with col2:
        ingredients_images = st.file_uploader(
            "재료 이미지를 업로드하세요:",
            type=["jpg", "png", "jpeg"],
            accept_multiple_files=True,
            key="ingredients"
        )

    return ingredients_text, ingredients_images


def render_seasonings_input():
    """Render seasonings input section"""
    placeholder_text = """Ex)
소금
설탕
..."""
    seasonings = st.text_area(
        '조미료를 입력하세요 (줄바꿈으로 구분):',
        placeholder=placeholder_text,
        height=100
    )
    return seasonings


def render_tools_inputs():
    """Render cooking tools input section"""
    col3, col4 = st.columns(2)

    with col3:
        placeholder_text = """Ex)
후라이팬
냄비
..."""
        tools_text = st.text_area(
            '조리도구를 입력하세요 (줄바꿈으로 구분):',
            placeholder=placeholder_text,
            height=100
        )

    with col4:
        tools_images = st.file_uploader(
            "조리도구 이미지를 업로드하세요:",
            type=["jpg", "png", "jpeg"],
            accept_multiple_files=True,
            key="tools"
        )

    return tools_text, tools_images


def render_preferences():
    """Render preference selection section"""
    difficulty = st.slider('요리 난이도를 선택하세요:', 1, 5, 3)

    cuisine_options = ["선택 안함", "한식", "중식", "양식", "일식", "기타"]
    cuisine = st.selectbox('세계 음식 종류를 선택하세요:', cuisine_options)

    if cuisine == "기타":
        cuisine = st.text_input('세계 음식 종류를 직접 입력하세요:')

    diet = st.radio('다이어트/벌크업/상관없음:', ('다이어트', '벌크업', '상관없음'))
    health = st.checkbox('건강을 고려한 음식')

    return difficulty, cuisine, diet, health


def render_footer():
    """Render the app footer"""
    st.markdown("---")
    st.markdown("Made by Myophily, 2024")


def create_recipe_prompt(ingredients: str, seasonings: str, tools: str,
                         difficulty: int, cuisine: str, diet: str, health: bool) -> str:
    """
    Create a prompt for recipe generation

    Args:
        ingredients: Available ingredients
        seasonings: Available seasonings
        tools: Available cooking tools
        difficulty: Cooking difficulty level
        cuisine: Cuisine type preference
        diet: Diet goal
        health: Whether to consider health

    Returns:
        Formatted prompt string
    """
    return f"""
재료: {ingredients}
조미료: {seasonings}
조리도구: {tools}
난이도: {difficulty}
음식 종류: {cuisine}
식단 목적: {diet}
건강 고려: {'예' if health else '아니오'}

위 정보를 바탕으로 적합한 요리 1가지를 추천해주세요. 다음 형식으로 답변해주세요:

[추천 요리 이름]

추천 이유:
(이유 설명)

레시피:
1. (조리 단계)
2. (조리 단계)
...
"""
