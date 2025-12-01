class ProfileAgent:
def __init__(self, model):
self.model = model


def run(self, user_input: str) -> dict:
prompt = f"Extract the user's fitness goals, preferences, health details, and constraints from this text. Return JSON only.\n\nInput: {user_input}""
response = self.model.generate_content(prompt)
return response.text
