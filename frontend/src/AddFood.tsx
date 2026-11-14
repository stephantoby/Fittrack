import { useState } from "react";
import type { NewFood, Food } from "./types";

export default function AddFood({
  onFoodAdded,
}: {
  onFoodAdded: (newFood: Food) => void;
}) {
  const [name, setName] = useState("");
  const [calories, setCalories] = useState("");
  const [protein, setProtein] = useState("");
  const [servingSize, setServingSize] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [submitError, setSubmitError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setIsLoading(true);
    setSubmitError(null);
    const newFood: NewFood = {
      name,
      calories: Number(calories),
      protein: Number(protein),
      serving_size: Number(servingSize),
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/foods/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newFood),
      });

      if (!response.ok) {
        throw new Error("Failed to add food");
      }
      const data = await response.json();
      console.log("Food added successfully:", data);
      onFoodAdded(data); // Call the callback function to update the food list

      setName("");
      setCalories("");
      setProtein("");
      setServingSize("");
    } catch (err) {
      console.error("Error adding food:", err);
      setSubmitError("Could not add food.");
    } finally {
      setIsLoading(false);
    }
  };
  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="name">
          Name:
        </label>

        <input placeholder = "e.g., Egg Salad" min="0" id="name"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="calories">
          Calories:
        </label>
        <input placeholder = "e.g., 150" min="0" id="calories"
          type="number"
          value={calories}
          onChange={(e) => setCalories(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="protein">
          Protein:
        </label>
        <input placeholder = "e.g., 10" min="0" id="protein"
          type="number"
          value={protein}
          onChange={(e) => setProtein(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="serving_size">
          Serving Size (g):
        </label>
        <input placeholder = "e.g., 100" min="0" id="serving_size"
          type="number"
          value={servingSize}
          onChange={(e) => setServingSize(e.target.value)}
          required
        />
      </div>
      {submitError && <p>{submitError}</p>}
      <button type="submit" disabled={isLoading}>
        {isLoading ? "Adding..." : "Add Food"}
      </button>
    </form>
  );
}
