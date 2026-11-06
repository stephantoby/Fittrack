import { useState, useEffect } from "react";

type Food = {
    id: number;
    name: string;
    calories: number;
    protein: number;
    serving_size: number;
};

function FoodLibrary(){
    const [foods, setFoods] = useState<Food[]>([]);
    useEffect(() => {
        async function loadFoods(){
            try{
                const response = await fetch('http://127.0.0.1:8000/foods/');

                if (!response.ok){
                    throw new Error('Failed to fetch foods');
                }
                const data: Food[] = await response.json();

                setFoods(data);
            }catch (error){
                console.error('Error loading foods', error);
            }
        }
        loadFoods();

    },[]);

    return(
        <div>
            <h2>Food library</h2>
            <p>Foods loaded: {foods.length}</p>
            {foods.map((food) => (
                <div key={food.id}>
                    <h3>{food.name}</h3>
                    <p>Calories: {food.calories}</p>
                    <p>Protein: {food.protein}</p>
                    <p>Serving Size: {food.serving_size}</p>
                </div>
            ))}
        </div>
    );
}

export default FoodLibrary
