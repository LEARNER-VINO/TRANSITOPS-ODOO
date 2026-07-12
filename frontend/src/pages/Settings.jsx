import Layout from "../components/Layout";

function Settings() {
  return (
    <Layout>
      <h1 className="text-3xl font-bold mb-6">
        Settings
      </h1>

      <div className="bg-white rounded-xl shadow p-8 space-y-5">

        <div>
          <label className="block font-semibold mb-2">
            Company Name
          </label>

          <input
            type="text"
            defaultValue="TransitOps"
            className="border rounded-lg p-3 w-full"
          />
        </div>

        <div>
          <label className="block font-semibold mb-2">
            Notification Email
          </label>

          <input
            type="email"
            defaultValue="admin@transitops.com"
            className="border rounded-lg p-3 w-full"
          />
        </div>

        <button className="bg-blue-600 text-white px-6 py-3 rounded-lg">
          Save Settings
        </button>

      </div>
    </Layout>
  );
}

export default Settings;