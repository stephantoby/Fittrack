from validation import *
from foods import *
from entries import *
from calculations import *
from goals import *
from storage import *


def main():

    foods = load_foods()
    food_entries = load_log()
    daily_goals = load_goals()

    while True:
         print("================================")
         print("        Food Tracker!      ")
         print("================================\n")
         print("1. Add Food")
         print("2. Update Food")
         print("3. View Foods")
         print("4. Delete Food")
         print("5. Log Foods")
         print("6. Exit\n")
         print("--------------------------------")

         try:
             choice = int(input("Choose an option: "))
         except ValueError:
             print("Invalid input. Please enter a number.")
             continue
         print("\n")


         if choice == 1:
             
             add_food()
             input(f"\nPress Enter to return to the main menu...")

         elif choice == 2:

             if update_food() == None:
                 input("Press Enter to return to the main menu...\n")
             else:
                 input(f"\nFood has been updated. Press Enter to return to the main menu...")
                 
         elif choice == 3:
            view_foods()
            input(f"\nPress Enter to return to the main menu...")

         elif choice == 4:
             delete_food()
             input(f"\nPress Enter to return to the main menu...")

         elif  choice == 5:
             while True:
                print("================================")
                print("        Food Log Menu!      ")
                print("================================\n")
                print("1. Add Food Log")
                print("2. View Food Log")
                print("3. Calculate Daily Calories and Protein")
                print("4. Update Food Entries")
                print("5. Delete Food Entries")
                print("6. Return to Main Menu\n")

                try:
                    choice = int(input("Choose an option: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                print("\n")

                if choice == 1:
                    log_food()
                elif choice == 2:
                    view_food_log(food_entries)
                
                elif choice == 3:
                   while True:
                       print("================================")
                       print("        Daily Totals!      ")
                       print("================================\n")
                       print("1. Calculate Daily Calories and Protein")
                       print("2. Add Daily calorie goal and protein goal")
                       print("3. View Daily Totals with Goals")
                       print("4. Return\n")

                       try:
                           choice = int(input("Choose an option: "))
                       except ValueError:
                           print("Invalid input. Please enter a number.")
                           continue
                       print("\n")
                       
                       if choice == 1:
                           total_calories, total_protein = calculate_totals(food_entries)
                           print("========Daily Totals========")
                           print(f"\nCalories: {total_calories} kcal")
                           print(f"Protein: {total_protein} g")
                           print(f"Foods Logged: {len(food_entries)}")
                           print("--------------------------------")
                           input(f"\nPress Enter to return to the main menu...")
                           
                       elif choice == 2:
                            daily_calorie_goal = get_valid_calories("Enter your daily calorie goal: ")
                            daily_protein_goal = get_valid_protein("Enter your daily protein goal: ")
    
                            total_calories, total_protein = calculate_totals(food_entries)
    
                            print("\n========Daily Totals========")
                            print(f"\nCalories: {total_calories} kcal / Goal: {daily_calorie_goal} kcal")
                            print(f"Protein: {total_protein} g / Goal: {daily_protein_goal} g")
                            print(f"Foods Logged: {len(food_entries)}")
                            print("--------------------------------")
                            print(f"\nCalories remaining: {daily_calorie_goal - total_calories}")
                            print(f"Protein remaining: {daily_protein_goal - total_protein}")
                            input(f"\nPress Enter to return to the main menu...")

                            daily_goal = {
                                "daily_calorie_goal": daily_calorie_goal,
                                "daily_protein_goal": daily_protein_goal
                            }

                            daily_goals.append(daily_goal)
                            save_goals(daily_goals)

                       elif choice == 3:
                           view_goals(daily_goals)

                       elif choice == 4:
                            break
                       else:
                            print("Invalid choice. Please try again.")                               
                        
                elif choice == 4:
                    update_entry(food_entries,foods)
                    save_log(food_entries)
                
                elif choice == 5:
                    delete_food(food_entries)
                    save_log(food_entries)

                elif choice == 6:
                    break

                else:
                    print("Invalid choice. Please try again.")

    
         elif choice == 6:
            break
         
         else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
