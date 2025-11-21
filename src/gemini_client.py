"""Gemini API client for recipe generation"""

import streamlit as st
import google.generativeai as genai


class GeminiClient:
    """Client for interacting with Google Gemini API"""

    def __init__(self, api_key: str):
        """Initialize Gemini client with API key"""
        self.api_key = api_key
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash-lite')

    def generate_response(self, prompt: str, images: list = None) -> str:
        """
        Generate a response from Gemini model

        Args:
            prompt: Text prompt for the model
            images: Optional list of image byte arrays

        Returns:
            Generated text response
        """
        try:
            if images:
                image_parts = [
                    {"mime_type": "image/jpeg", "data": img_byte_arr}
                    for img_byte_arr in images
                ]
                response = self.model.generate_content([prompt] + image_parts)
            else:
                response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            st.error(f"An error occurred while generating the response: {str(e)}")
            return ""

    def process_uploaded_images(self, uploaded_files, prompt: str) -> str:
        """
        Process uploaded image files and generate response

        Args:
            uploaded_files: List of uploaded file objects
            prompt: Prompt to send with images

        Returns:
            Generated text response
        """
        if not uploaded_files:
            return ""

        try:
            image_byte_arrays = [
                uploaded_file.getvalue()
                for uploaded_file in uploaded_files
            ]
            return self.generate_response(prompt, image_byte_arrays)
        except Exception as e:
            st.error(f"An error occurred while processing the images: {str(e)}")
            return ""
