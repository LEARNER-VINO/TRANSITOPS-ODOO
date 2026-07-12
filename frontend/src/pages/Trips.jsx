import Layout from "../components/Layout";

function Trips() {
  const trips = [
    {
      id: "TR001",
      vehicle: "TN38 AB2456",
      driver: "Rahul",
      route: "Coimbatore → Chennai",
      status: "Active",
    },
    {
      id: "TR002",
      vehicle: "TN66 CD8712",
      driver: "Priya",
      route: "Salem → Madurai",
      status: "Completed",
    },
    {
      id: "TR003",
      vehicle: "TN37 EF9921",
      driver: "Arun",
      route: "Erode → Trichy",
      status: "Cancelled",
    },
  ];

  return (
    <Layout>
      <div className="space-y-6">

        <h1 className="text-3xl font-bold">
          Trips
        </h1>

        <div className="bg-white rounded-xl shadow-md p-6">

          <table className="w-full">

            <thead className="bg-gray-100">

              <tr>
                <th className="p-3 text-left">Trip ID</th>
                <th className="p-3 text-left">Vehicle</th>
                <th className="p-3 text-left">Driver</th>
                <th className="p-3 text-left">Route</th>
                <th className="p-3 text-left">Status</th>
              </tr>

            </thead>

            <tbody>

              {trips.map((trip) => (
                <tr key={trip.id} className="border-b">

                  <td className="p-3">{trip.id}</td>
                  <td className="p-3">{trip.vehicle}</td>
                  <td className="p-3">{trip.driver}</td>
                  <td className="p-3">{trip.route}</td>

                  <td className="p-3">
                    <span
                      className={`px-3 py-1 rounded-full text-white text-sm ${
                        trip.status === "Active"
                          ? "bg-green-500"
                          : trip.status === "Completed"
                          ? "bg-blue-500"
                          : "bg-red-500"
                      }`}
                    >
                      {trip.status}
                    </span>
                  </td>

                </tr>
              ))}

            </tbody>

          </table>

        </div>

      </div>
    </Layout>
  );
}

export default Trips;