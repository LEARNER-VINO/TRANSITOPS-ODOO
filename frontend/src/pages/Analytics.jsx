import Layout from "../components/Layout";

function Analytics() {
  return (
    <Layout>
      <h1 className="text-3xl font-bold mb-6">Analytics</h1>

      <div className="grid grid-cols-2 gap-6">

        <div className="bg-white p-6 rounded-xl shadow">
          <h2 className="font-semibold text-xl mb-3">
            Fuel Efficiency
          </h2>

          <div className="h-56 flex items-center justify-center border-2 border-dashed rounded-lg text-gray-400">
            📈 Chart Coming Soon
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow">
          <h2 className="font-semibold text-xl mb-3">
            Revenue Analytics
          </h2>

          <div className="h-56 flex items-center justify-center border-2 border-dashed rounded-lg text-gray-400">
            📊 Chart Coming Soon
          </div>
        </div>

      </div>
    </Layout>
  );
}

export default Analytics;