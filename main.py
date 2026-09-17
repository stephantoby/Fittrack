from validation import *
from foods import *
from entries import *
from calculations import *
from goals import *
from storage import *
from db import get_connection


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
                    view_food_log()
                elif choice == 3:
                   while True:
                       print("================================")
                       print("        Daily Totals!      ")
                       print("================================\n")
                       print("1. Calculate total calories and protein")
                       print("2. Log Body Weight, Daily Calorie and Protein Goal")
                       print("3. View Daily Totals with Goals")
                       print("4. Return\n")
                       print("5. View how much remaining")
                      

                       try:
                           choice = int(input("Choose an option: "))
                       except ValueError:
                           print("Invalid input. Please enter a number.")
                           continue
                       print("\n")
                       
                       if choice == 1:
                           
                           total_calories, total_protein = calculate_totals()
                           print("========Daily Totals========")
                           print(f"\nCalories: {total_calories} kcal")
                           print(f"Protein: {total_protein} g")
                           print(f"Foods Logged: {len(food_entries)}")
                           print("--------------------------------")
                           input(f"\nPress Enter to return to the main menu...")
                           
                       elif choice == 2:
                            while True:
                                goal_type = input("Enter goal type (Bulk/Cut/Maintain): ").strip()
                                if goal_type == "":
                                    print("\n Goal type cannot be empty. Please enter a valid type.")
                                    continue
                                else:
                                    break

                            body_weight = get_valid_weight("Enter your body weight(kg): ") 
                            daily_calorie_goal = get_valid_calories("Enter your daily calorie goal: ")
                            daily_protein_goal = get_valid_protein("Enter your daily protein goal: ")
    
                            total_calories, total_protein = calculate_totals()

                            connection = get_connection()
                            cursor = connection.cursor()
                            
                            cursor.execute('''
                            INSERT INTO goals (goal_type, target_weight, daily_calorie_goal, daily_protein_goal)
                            VALUES (?,?,?,?)
                            ''', (goal_type, body_weight, daily_calorie_goal, daily_protein_goal))
                            
                            connection.commit()
                            connection.close()

                            print("Successfully stored into the database")
    
    

                       elif choice == 3:
                           connection = get_connection()
                           cursor = connection.cursor()

                           cursor.execute('''
                           SELECT daily_calorie_goal, daily_protein_goal
                           FROM goals
                         ''')

                           result = cursor.fetchall()

                           row = result[0] 

                           daily_calorie_goal = row[0]
                           daily_protein_goal = row[1]

                           total_calories_consumed, total_protein_consumed = calculate_totals()

                           print("\n========Nutrition Remaining========")
                           print(f"\nCalories: {total_calories_consumed} kcal / Goal: {daily_calorie_goal} kcal")
                           print(f"Protein: {total_protein_consumed} g / Goal: {daily_protein_goal} g")
                           print("--------------------------------")
                           remaining_calories, remaining_protein = calculate_remaining(daily_calorie_goal, daily_protein_goal, total_calories_consumed, total_protein_consumed)
                           print(f"\nCalories remaining: {remaining_calories}")
                           print(f"Protein remaining: {remaining_protein}")
                           input(f"\nPress Enter to return to the main menu...")

                       elif choice == 3:
                           view_goals(daily_goals)

                       elif choice == 4:
                            break

                       elif choice == 5:
                           
                           print("\n========Daily Totals========")
                           print(f"\n Current Weight: {body_weight}")
                           print(f"\nCalories: {total_calories} kcal / Goal: {daily_calorie_goal} kcal")
                           
                       else:
                            print("Invalid choice. Please try again.")                               
                        
                elif choice == 4:
                    update_entry()
                
                elif choice == 5:
                    delete_food()


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
