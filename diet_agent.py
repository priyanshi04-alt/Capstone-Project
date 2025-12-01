class DietAgent:
def __init__(self, model):
self.model = model


def run(self, profile_data: dict) -> dict:
prompt = f"Create a personalized daily diet plan based on this profile JSON: {profile_data}. Return JSON only."
response = self.model.generate_content(prompt)
return response.text
