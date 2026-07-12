import Layout from "../components/Layout";

function Vehicles() {
  const vehicles = [
    {
      id: "TN38 AB2456",
      type: "Truck",
      driver: "Rahul",
      status: "Available",
    },
    {
      id: "TN66 CD8712",
      type: "Mini Truck",
      driver: "Priya",
      status: "On Trip",
    },
    {
      id: "TN37 EF9921",
      type: "Van",
      driver: "Arun",
      status: "Maintenance",
    },
  ];

  return (
    <Layout>
      <div className="space-y-6">

        <h1 className="text-3xl font-bold">
          Vehicles
        </h1>

        <div className="bg-white rounded-xl shadow-md p-6">

          <table className="w-full">

            <thead className="bg-gray-100">

              <tr>
                <th className="p-3 text-left">Vehicle No</th>
                <th className="p-3 text-left">Type</th>
                <th className="p-3 text-left">Driver</th>
                <th className="p-3 text-left">Status</th>
              </tr>

            </thead>

            <tbody>

              {vehicles.map((v) => (
                <tr key={v.id} className="border-b">

                  <td className="p-3">{v.id}</td>
                  <td className="p-3">{v.type}</td>
                  <td className="p-3">{v.driver}</td>

                  <td className="p-3">

                    <span
                      className={`px-3 py-1 rounded-full text-white text-sm ${
                        v.status === "Available"
                          ? "bg-green-500"
                          : v.status === "On Trip"
                          ? "bg-blue-500"
                          : "bg-red-500"
                      }`}
                    >
                      {v.status}
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

export default Vehicles;