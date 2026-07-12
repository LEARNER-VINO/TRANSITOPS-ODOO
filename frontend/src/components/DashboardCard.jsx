function DashboardCard({ title, value, color }) {
  return (
    <div
      className="bg-white rounded-2xl shadow-lg p-6 border-l-8 hover:scale-105 transition duration-300"
      style={{ borderColor: color }}
    >
      <p className="text-gray-500 text-sm font-medium">
        {title}
      </p>

      <h2 className="text-4xl font-bold mt-3">
        {value}
      </h2>

      <p className="text-green-600 text-sm mt-4">
        ▲ Updated Today
      </p>
    </div>
  );
}

export default DashboardCard;