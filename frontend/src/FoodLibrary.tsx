import { useState, useEffect } from "react";
import AddFood from "./AddFood";
import type { Food } from "./types";

function FoodLibrary() {
  const [foods, setFoods] = useState<Food[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);


  useEffect(() => {
    async function loadFoods() {
      setIsLoading(true);
      try {
        const response = await fetch("http://127.0.0.1:8000/foods/");

        if (!response.ok) {
          throw new Error("Failed to fetch foods");
        }
        const data: Food[] = await response.json();

        setFoods(data);
      } catch (err) {
        console.error("Error loading foods", err);
        setError("Could not load foods.");
      } finally {
        setIsLoading(false);
      }
    }
    loadFoods();
  }, []);

  function handleFoodAdded(newFood: Food){
    setFoods((prevFoods) => [...prevFoods, newFood]);
  }
  return (
    <div>
      <h2>Food library</h2>
      <AddFood onFoodAdded={(newFood) => handleFoodAdded(newFood)} />
      {error && <p>{error}</p>}
      {isLoading && <p>Loading foods...</p>}
      {!isLoading && !error && (
        <div>
          <p>Foods loaded: {foods.length}</p>
          {foods.map((food) => (
            <div key={food.id}>
              <h3>{food.name}</h3>
              <p>Calories: {food.calories}</p>
              <p>Protein: {food.protein}</p>
              <p>Serving Size: {food.serving_size} g</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default FoodLibrary;
