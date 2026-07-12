import Layout from "../components/Layout";

function Drivers() {
  const drivers = [
    {
      id: 1,
      name: "Rahul",
      vehicle: "TN38AB2456",
      status: "On Trip",
      phone: "9876543210",
    },
    {
      id: 2,
      name: "Priya",
      vehicle: "TN66CD8712",
      status: "Available",
      phone: "9876543211",
    },
    {
      id: 3,
      name: "Arun",
      vehicle: "TN37EF9921",
      status: "Leave",
      phone: "9876543212",
    },
  ];

  return (
    <Layout>
      <h1 className="text-3xl font-bold mb-6">Drivers</h1>

      <div className="bg-white rounded-xl shadow p-6">
        <table className="w-full">
          <thead className="bg-gray-100">
            <tr>
              <th className="text-left p-3">Name</th>
              <th className="text-left p-3">Vehicle</th>
              <th className="text-left p-3">Phone</th>
              <th className="text-left p-3">Status</th>
            </tr>
          </thead>

          <tbody>
            {drivers.map((driver) => (
              <tr key={driver.id} className="border-b">
                <td className="p-3">{driver.name}</td>
                <td className="p-3">{driver.vehicle}</td>
                <td className="p-3">{driver.phone}</td>
                <td className="p-3">{driver.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Layout>
  );
}

export default Drivers;