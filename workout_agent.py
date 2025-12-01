class WorkoutAgent:
def __init__(self, model):
self.model = model


def run(self, profile_data: dict, diet_data: dict) -> dict:
prompt = (
f"Generate a workout routine tailored to the user based on: \n"
f"Profile: {profile_data}\n"
f"Diet Plan: {diet_data}\n"
f"Return JSON only."
)
response = self.model.generate_content(prompt)
return response.text
