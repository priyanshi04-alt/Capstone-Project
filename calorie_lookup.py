# tools/calorie_lookup.py
"""
Simple offline calorie lookup tool.
Returns approximate calories for common food items and supports
serving-size scaling and meal aggregation.
"""

_DEFAULT_DB = {
    "oats (1 cup)": 300,
    "banana (1 medium)": 105,
    "almond milk (1 cup)": 30,
    "brown rice (1 cup)": 215,
    "dal (1 cup)": 230,
    "paneer (100g)": 265,
    "quinoa (1 cup)": 222,
    "mixed salad (1 cup)": 25,
    "egg (1 large)": 78,
    "chicken breast (100g)": 165,
    "lentils (1 cup cooked)": 230,
    "apple (1 medium)": 95
}

def lookup_calories(item_name: str, servings: float = 1.0, db: dict = None) -> dict:
    """
    Return approximate calorie info for an item.
    Returns dict: { "item": ..., "servings": ..., "calories_per_serving": ..., "total_calories": ... }
    """
    if db is None:
        db = _DEFAULT_DB

    # Normalize key by simple matching (case-insensitive, substring match)
    key = None
    item_lower = item_name.strip().lower()
    for k in db.keys():
        if item_lower in k.lower() or k.lower() in item_lower:
            key = k
            break

    if key is None:
        # fallback estimate: 200 kcal per serving
        calories_per_serving = 200
        found_key = None
    else:
        calories_per_serving = db[key]
        found_key = key

    total = int(round(calories_per_serving * servings))

    return {
        "query": item_name,
        "matched_item": found_key,
        "servings": servings,
        "calories_per_serving": calories_per_serving,
        "total_calories": total
    }

def aggregate_meal(items: list, db: dict = None) -> dict:
    """
    items: list of tuples (item_name, servings)
    returns: dict with breakdown + total calories
    """
    breakdown = []
    total = 0
    for name, servings in items:
        info = lookup_calories(name, servings, db=db)
        breakdown.append(info)
        total += info["total_calories"]

    return {"breakdown": breakdown, "total_calories": total}
