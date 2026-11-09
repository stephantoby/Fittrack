type NutritionCardProps = {
  label: string;
  value: string;
};

function NutritionCard({label, value}: NutritionCardProps) {
  return (
    <div>
      <h2>{label}</h2>
      <p>{value}</p>
    </div>  
  );
}

export default NutritionCard;