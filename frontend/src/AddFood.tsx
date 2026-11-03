import {useState} from 'react';

type Food = {
    name: string;
    calories: number;
    protein: number;
    serving_size: number;
}

export default function AddFood(){
    const [name, setName] = useState("");
    const [calories, setCalories] = useState(0);
    const [protein, setProtein] = useState(0);
    const [serving_size, setServingSize] = useState(0);
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setIsLoading(true);
        const newFood: Food = {
            name,
            calories,
            protein,
            serving_size
        };

        try{
            const response = await fetch("http://127.0.0.1:8000/foods/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(newFood),
            });

            if (!response.ok) {
                throw new Error('Failed to add food');
            }
            const data = await response.json();
            console.log("Food added successfully:", data);

            setName("");
            setCalories(0);
            setProtein(0);
            setServingSize(0);

        } catch (error) {
            console.error('Error adding food:', error);
        } finally {
            window.location.reload();
            setIsLoading(false);
        }
    };
    return (
        <form onSubmit = {handleSubmit}>
            <div>
                <input 
                type= "text"
                value={name}
                onChange={(e)=> setName(e.target.value)}
                required
                />
            </div>
            <div>
                <input 
                type= "number"
                value={calories}
                onChange={(e)=> setCalories(Number(e.target.value))}
                required
                />
            </div>
            <div>
                <input 
                type= "number"
                value={protein}
                onChange={(e)=> setProtein(Number(e.target.value))}
                required
                />
            </div>
            <div>
                <input 
                type= "number"
                value={serving_size}
                onChange={(e)=> setServingSize(Number(e.target.value))}
                required
                />
            </div>
            <button type="submit" disabled={isLoading}>
                {isLoading ? "Adding..." : "Add Food"}
            </button>
        </form>
        );
}   

