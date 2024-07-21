import streamlit as st
import google.generativeai as genai

# API 키 설정
gemini_api_key = st.secrets["GEMINI_API_KEY"]

# Gemini 모델 설정
genai.configure(api_key=gemini_api_key)


def get_gemini_response(prompt, images=[]):
    model = genai.GenerativeModel('gemini-1.5-flash')
    try:
        if images:
            image_parts = [{"mime_type": "image/jpeg",
                            "data": img_byte_arr} for img_byte_arr in images]
            response = model.generate_content([prompt] + image_parts)
        else:
            response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while generating the response: {str(e)}")
        return ""


def process_uploaded_images(uploaded_files, prompt):
    if not uploaded_files:
        return ""

    try:
        image_byte_arrays = []
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.getvalue()
            image_byte_arrays.append(bytes_data)

        return get_gemini_response(prompt, image_byte_arrays)
    except Exception as e:
        st.error(f"An error occurred while processing the images: {str(e)}")
        return ""


# Streamlit 앱의 UI 구성
st.title('Fridge Breaker (냉장고 털어먹기)')

# 재료 입력
col1, col2 = st.columns(2)
with col1:
    ingredients_text = st.text_area('재료를 입력하세요 (줄바꿈으로 구분):', height=100)
with col2:
    ingredients_images = st.file_uploader(
        "재료 이미지를 업로드하세요:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# 조미료 입력
seasonings = st.text_area('조미료를 입력하세요 (줄바꿈으로 구분):', height=100)

# 조리도구 입력
col3, col4 = st.columns(2)
with col3:
    tools_text = st.text_area('조리도구를 입력하세요 (줄바꿈으로 구분):', height=100)
with col4:
    tools_images = st.file_uploader("조리도구 이미지를 업로드하세요:", type=[
                                    "jpg", "png", "jpeg"], accept_multiple_files=True)

# 요리 난이도 선택
difficulty = st.slider('요리 난이도를 선택하세요:', 1, 5, 3)

# 세계 음식 선택
cuisine_options = ["선택 안함", "한식", "중식", "양식", "일식", "기타"]
cuisine = st.selectbox('세계 음식 종류를 선택하세요:', cuisine_options)
if cuisine == "기타":
    cuisine = st.text_input('세계 음식 종류를 직접 입력하세요:')

# 다이어트/벌크업/상관없음 선택
diet = st.radio('다이어트/벌크업/상관없음:', ('다이어트', '벌크업', '상관없음'))

# 건강을 고려한 음식
health = st.checkbox('건강을 고려한 음식')

col5, col6 = st.columns([3, 1])
with col5:
    if st.button('레시피 받기'):
        ingredients_from_images = process_uploaded_images(
            ingredients_images, "이 이미지에서 보이는 식재료들을 쉼표로 구분하여 나열해주세요.") if 'ingredients_images' in locals() else ""
        tools_from_images = process_uploaded_images(
            tools_images, "이 이미지에서 보이는 조리도구들을 쉼표로 구분하여 나열해주세요.") if 'tools_images' in locals() else ""

        all_ingredients = f"{ingredients_text}, {ingredients_from_images}".strip(
            ', ')
        all_tools = f"{tools_text}, {tools_from_images}".strip(', ')

        prompt = f"""
        재료: {all_ingredients}
        조미료: {seasonings}
        조리도구: {all_tools}
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

        with st.spinner('레시피 생성 중...'):
            gemini_recipe = get_gemini_response(prompt)

        st.subheader('Gemini를 통한 추천 레시피:')
        st.markdown(gemini_recipe)

with col6:
    st.markdown('Powered By GEMINI')

st.markdown("---")
st.markdown("Made by Myophily")
