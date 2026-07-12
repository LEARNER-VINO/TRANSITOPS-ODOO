function DashboardCard({ title, value, color }) {
  return (
    <div
      className="bg-white rounded-xl shadow-md p-6 border-l-4 hover:shadow-xl transition duration-300"
      style={{ borderColor: color }}
    >
      <p className="text-gray-500 text-sm">{title}</p>

      <h2 className="text-4xl font-bold mt-3">{value}</h2>
    </div>
  );
}

export default DashboardCard;