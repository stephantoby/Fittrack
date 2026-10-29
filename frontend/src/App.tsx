import './App.css'
import NutritionCard from './NutritionCard';
import { useState } from 'react';
import FoodLibrary from './FoodLibrary';

function App() {
  const [calories, setCalories] = useState(0);
  const calorieGoal = 2500;
  const remaining = calorieGoal - calories;
  const [amount, setAmount] = useState("");
  const [error, setError] = useState("");

  return (
    <>
        <NutritionCard label="Calories" value= {`${calories} kcal`} />
        <NutritionCard label="Protein" value="125 g" />
        <NutritionCard label="Remaining" value={`${remaining} kcal`} />
        <FoodLibrary/>
        <button onClick={() =>{
          const calorieAmount = Number(amount);
          if (calorieAmount > 0) {
          setCalories(calories + calorieAmount);
          setAmount("");
          setError("");
          }else{
            setError("Please enter a valid positive number.");
          }
        }}>
            Add calories
          </button>
        <button onClick={() => {
          setCalories(0);
          setAmount("")
          }}>Reset</button>
        
        <input 
          value = {amount} 
          onChange={(event) => setAmount(event.target.value)}
        />
        <p>{error}</p>
    </>
  );
}

export default App
