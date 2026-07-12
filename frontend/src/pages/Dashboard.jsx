import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import DashboardCard from "../components/DashboardCard";
import { getDashboard } from "../services/api";

import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

function Dashboard() {
  const [dashboard, setDashboard] = useState({
    active_vehicles: 0,
    ongoing_trips: 0,
    alerts: 0,
  });

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchDashboard() {
      try {
        const data = await getDashboard();

        console.log("Dashboard Data:", data);

        setDashboard(data);
      } catch (error) {
        console.error("Error fetching dashboard:", error);
      } finally {
        setLoading(false);
      }
    }

    // THIS WAS MISSING
    fetchDashboard();
  }, []);

  const chartData = [
    { month: "Jan", trips: 18 },
    { month: "Feb", trips: 24 },
    { month: "Mar", trips: 32 },
    { month: "Apr", trips: 28 },
    { month: "May", trips: 38 },
    { month: "Jun", trips: 45 },
  ];

  if (loading) {
    return (
      <Layout>
        <div className="flex justify-center items-center h-[70vh] text-2xl font-semibold">
          Loading Dashboard...
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="space-y-8">

        {/* Dashboard Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

          <DashboardCard
            title="Active Vehicles"
            value={dashboard.active_vehicles}
            color="#16a34a"
          />

          <DashboardCard
            title="Ongoing Trips"
            value={dashboard.ongoing_trips}
            color="#2563eb"
          />

          <DashboardCard
            title="Alerts"
            value={dashboard.alerts}
            color="#dc2626"
          />

          <DashboardCard
            title="System Status"
            value="Online"
            color="#9333ea"
          />

        </div>

        {/* Fleet Analytics */}
        <div className="bg-white rounded-xl shadow-md p-6">

          <h2 className="text-xl font-semibold mb-5">
            Fleet Analytics
          </h2>

          <ResponsiveContainer width="100%" height={320}>

            <LineChart data={chartData}>

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="month" />

              <YAxis />

              <Tooltip />

              <Line
                type="monotone"
                dataKey="trips"
                stroke="#2563eb"
                strokeWidth={4}
              />

            </LineChart>

          </ResponsiveContainer>

        </div>

        {/* Recent Trips */}
        <div className="bg-white rounded-xl shadow-md p-6">

          <h2 className="text-xl font-semibold mb-5">
            Recent Trips
          </h2>

          <table className="w-full">

            <thead className="bg-gray-100">

              <tr>
                <th className="p-3 text-left">Vehicle</th>
                <th className="p-3 text-left">Driver</th>
                <th className="p-3 text-left">Route</th>
                <th className="p-3 text-left">Status</th>
              </tr>

            </thead>

            <tbody>

              <tr className="border-b hover:bg-gray-50">
                <td className="p-3">TN38 AB2456</td>
                <td className="p-3">Rahul</td>
                <td className="p-3">Coimbatore → Chennai</td>
                <td className="p-3">
                  <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm">
                    Active
                  </span>
                </td>
              </tr>

              <tr className="border-b hover:bg-gray-50">
                <td className="p-3">TN66 CD8712</td>
                <td className="p-3">Priya</td>
                <td className="p-3">Salem → Madurai</td>
                <td className="p-3">
                  <span className="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm">
                    Maintenance
                  </span>
                </td>
              </tr>

              <tr className="hover:bg-gray-50">
                <td className="p-3">TN37 EF9921</td>
                <td className="p-3">Arun</td>
                <td className="p-3">Erode → Trichy</td>
                <td className="p-3">
                  <span className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm">
                    On Route
                  </span>
                </td>
              </tr>

            </tbody>

          </table>

        </div>

      </div>
    </Layout>
  );
}

export default Dashboard;