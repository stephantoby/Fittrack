type NutritionCardProps = {
  label: string;
  value: string;
};

function NutritionCard(props: NutritionCardProps) {
  return (
    <div>
      <h2>{props.label}</h2>
      <p>{props.value}</p>
    </div>
  );
}

export default NutritionCard;