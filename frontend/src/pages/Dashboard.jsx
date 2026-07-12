import Layout from "../components/Layout";
import DashboardCard from "../components/DashboardCard";

function Dashboard() {
  return (
    <Layout>
      <div className="space-y-8">

        {/* Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

          <DashboardCard title="Active Trips" value="124" color="#2563eb" />
          <DashboardCard title="Vehicles" value="58" color="#16a34a" />
          <DashboardCard title="Drivers" value="42" color="#ea580c" />
          <DashboardCard title="Fuel Usage" value="82%" color="#9333ea" />

        </div>

        {/* Analytics */}
        <div className="bg-white rounded-xl shadow-md p-6">

          <h2 className="text-xl font-semibold mb-4">
            Fleet Analytics
          </h2>

          <div className="h-80 rounded-lg border-2 border-dashed border-gray-300 flex items-center justify-center text-2xl text-gray-400">
            📈 Analytics Chart
          </div>

        </div>

        {/* Recent Trips */}
        <div className="bg-white rounded-xl shadow-md p-6">

          <h2 className="text-xl font-semibold mb-4">
            Recent Trips
          </h2>

          <table className="w-full">

            <thead className="bg-gray-100">

              <tr>

                <th className="text-left p-3">Vehicle</th>
                <th className="text-left p-3">Driver</th>
                <th className="text-left p-3">Route</th>
                <th className="text-left p-3">Status</th>

              </tr>

            </thead>

            <tbody>

              <tr className="border-b">
                <td className="p-3">TN38 AB2456</td>
                <td className="p-3">Rahul</td>
                <td className="p-3">Coimbatore → Chennai</td>
                <td className="p-3 text-green-600 font-semibold">Active</td>
              </tr>

              <tr className="border-b">
                <td className="p-3">TN66 CD8712</td>
                <td className="p-3">Priya</td>
                <td className="p-3">Salem → Madurai</td>
                <td className="p-3 text-yellow-600 font-semibold">
                  Maintenance
                </td>
              </tr>

              <tr>
                <td className="p-3">TN37 EF9921</td>
                <td className="p-3">Arun</td>
                <td className="p-3">Erode → Trichy</td>
                <td className="p-3 text-blue-600 font-semibold">On Route</td>
              </tr>

            </tbody>

          </table>

        </div>

      </div>
    </Layout>
  );
}

export default Dashboard;