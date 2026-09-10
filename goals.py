def view_goals(daily_goals):
    if not daily_goals:
        print("\nNo daily goals have been set yet.")
        return
    
    print("================================")
    print("          Daily Goals!       ")
    print("================================\n")

    for number, goal in enumerate(daily_goals, start= 1):
        print(f"{number}.")
        print(f"Daily Calorie Goal: {goal['daily_calorie_goal']} kcal")
        print(f"Daily Protein Goal: {goal['daily_protein_goal']} g")
        print("-----------------------------")
  