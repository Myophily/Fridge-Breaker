# Fridge Breaker (냉장고 털어먹기)

A Streamlit web application that helps you discover recipes based on ingredients available in your fridge using Google's Gemini AI.

## Features

- **Ingredient Input**: Enter ingredients via text or upload images
- **Cooking Tools**: Specify available cooking equipment
- **Customizable Preferences**:
  - Difficulty level selection (1-5)
  - Cuisine type (Korean, Chinese, Western, Japanese, etc.)
  - Diet goals (Weight loss, Bulking, or No preference)
  - Health-conscious option
- **AI-Powered Recommendations**: Powered by Google Gemini 1.5 Flash for intelligent recipe suggestions

## Prerequisites

- Python 3.11 or higher
- Google Gemini API key

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Fridge-Breaker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your API key:
   Create a `.streamlit/secrets.toml` file with:
   ```toml
   GEMINI_API_KEY = "your-api-key-here"
   ```

## Usage

Run the application:
```bash
streamlit run streamlit_app.py
```

The app will open in your default browser at `http://localhost:8501`

## How It Works

1. Input your available ingredients (text or images)
2. Add seasonings you have
3. Specify cooking tools available
4. Set your preferences (difficulty, cuisine type, diet goals)
5. Click "레시피 받기" (Get Recipe) to receive a personalized recipe recommendation

## Project Structure

```
Fridge-Breaker/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── app.py               # Main Streamlit application
│   ├── gemini_client.py     # Gemini API client
│   └── ui_components.py     # UI components and layouts
├── streamlit_app.py         # Entry point
├── requirements.txt         # Python dependencies
└── README.md
```

## Development

This project includes a devcontainer configuration for easy development in VS Code or GitHub Codespaces.

---

Made by Myophily, 2024
