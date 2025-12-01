# Capstone-Project
# FitLife Coach – Personalized Health Recommendation System  
### Kaggle × Google Agents Intensive — Capstone Project

---

## 🧠 Overview

**FitLife Coach** is a lightweight **offline multi-agent wellness assistant** that generates:
- Personalized **diet plans**
- Custom **workout routines**
- Structured **user profiles**

The system is designed to run **entirely inside Kaggle**, without:
❌ API keys  
❌ Paid LLMs  
❌ External internet access  

This makes the project fully reproducible and deployable in constrained environments.

---

## 🔗 Motivation

Most AI-based fitness apps depend on expensive AI models, cloud APIs, or complex deployments.  
For a competition environment like Kaggle, we need:

- Deterministic behavior  
- Zero external dependencies  
- Clear multi-agent logic  
- Explainability  
- Fast inference  

FitLife Coach is built exactly around these constraints.

---

## 🏗️ System Architecture

The system consists of **three offline agents**, connected in a simple pipeline:

### **1. Profile Agent**
Parses user text into a structured profile:
- Age  
- Gender  
- Fitness goal  
- Activity level  

### **2. Diet Agent**
Maps profile attributes to:
- Daily calorie target  
- Meal plan (breakfast / lunch / dinner)  
- Basic nutritional guidance  

### **3. Workout Agent**
Generates a workout plan based on:
- Activity level  
- Goal  
- Daily time availability (optional)  

### **Pipeline Flow**
```
User Input → Profile Agent → Diet Agent + Workout Agent → Combined Output
```

This ensures clarity, modularity, and interpretability.

---

## ⚙️ Offline Agent Logic

Each agent uses:
- Rule-based decision trees
- Template-based reasoning
- Keyword parsing

This provides:
- 100% reproducible output  
- Fast execution  
- No GPU/TPU needed  

---

## 🚀 How to Use (Notebook)

1. Open the notebook: **FitLife_Coach_Notebook.ipynb**  
2. Run all cells  
3. Enter a natural language user query such as:

```
I am a 25-year-old female, want to lose weight, activity level high.
```

4. The model outputs:

- User profile (structured)
- Diet plan
- Workout routine
- JSON export object

---

## 📊 Visualizations

The notebook includes:
- Mock calorie distribution chart
- Example intensity mapping
- Output tables for clarity

---

## 📦 Export Format (JSON)

```json
{
  "User Profile": {
    "age": 25,
    "gender": "female",
    "goal": "weight_loss",
    "activity": "high"
  },
  "Diet Plan": {
    "diet_plan": [
      "Breakfast: Oats + Fruits",
      "Lunch: 1 Roti + Dal + Salad",
      "Dinner: Vegetable Soup"
    ]
  },
  "Workout Plan": {
    "workout_plan": [
      "30-min brisk walk",
      "15-min HIIT",
      "Yoga – Surya Namaskar",
      "10-min cooldown"
    ]
  }
}
```

---

## 🧪 Evaluation

Since we are not using LLMs, evaluation is done via:

- **Rule coverage checks**  
- **Input → output consistency**  
- **Edge-case behaviour**  
- **Deterministic output test**  

---

## 📈 Future Improvements

- Add BMI & TDEE calculations  
- Add mental-health agent  
- Add meal macros computation  
- Replace rule-based engine with lightweight on-device LLM (when allowed)  
- Add UI using Streamlit  

---

## 🙌 Contributors

Priyanshi   
Kaggle User – Agents Intensive 2025

---

## 📜 License
MIT License.

