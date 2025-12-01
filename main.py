from agents.profile_agent import ProfileAgent
from agents.diet_agent import DietAgent
from agents.workout_agent import WorkoutAgent

def run_fitlife_system(user_input):
    print("\n=== FITLIFE AI MULTI-AGENT SYSTEM STARTED ===")

    # 1. Profile Agent
    profile_agent = ProfileAgent()
    user_profile = profile_agent.process(user_input)
    print("\n[Profile Agent Output]:")
    print(user_profile)

    # 2. Diet Agent
    diet_agent = DietAgent()
    diet_plan = diet_agent.generate_diet(user_profile)
    print("\n[Diet Agent Output]:")
    print(diet_plan)

    # 3. Workout Agent
    workout_agent = WorkoutAgent()
    workout_plan = workout_agent.generate_workout(user_profile)
    print("\n[Workout Agent Output]:")
    print(workout_plan)

    # Final Response
    final_pack = {
        "user_profile": user_profile,
        "diet_plan": diet_plan,
        "workout_plan": workout_plan
    }

    print("\n=== FINAL WELLNESS PACK GENERATED ===")
    return final_pack


if __name__ == "__main__":
    sample_user = """
    I am Priyanshi, 22 yrs old.
    Female, weight 58 kg, height 160 cm.
    My goal is weight loss and toning.
    I prefer vegetarian food, cannot eat eggs.
    I can work out 4 days a week.
    """

    result = run_fitlife_system(sample_user)
    print("\nFinal Output:\n", result)
