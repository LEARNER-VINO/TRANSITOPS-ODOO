import {
  FaTachometerAlt,
  FaTruck,
  FaRoute,
  FaUsers,
  FaChartLine,
  FaCog,
} from "react-icons/fa";

import { Link, useLocation } from "react-router-dom";

function Sidebar() {
  const location = useLocation();

  const menu = [
    { name: "Dashboard", path: "/dashboard", icon: <FaTachometerAlt /> },
    { name: "Vehicles", path: "/vehicles", icon: <FaTruck /> },
    { name: "Trips", path: "/trips", icon: <FaRoute /> },
    { name: "Drivers", path: "/drivers", icon: <FaUsers /> },
    { name: "Analytics", path: "/analytics", icon: <FaChartLine /> },
    { name: "Settings", path: "/settings", icon: <FaCog /> },
  ];

  return (
    <aside className="fixed left-0 top-0 h-screen w-64 bg-slate-900 text-white shadow-2xl">

      <div className="p-6 border-b border-slate-700">
        <h1 className="text-3xl font-bold text-blue-400">
          🚚 TransitOps
        </h1>

        <p className="text-sm text-slate-400 mt-2">
          Fleet Management System
        </p>
      </div>

      <nav className="mt-6 px-3">

        {menu.map((item) => (
          <Link
            key={item.name}
            to={item.path}
            className={`flex items-center gap-4 px-4 py-3 rounded-xl mb-2 transition duration-300 ${
              location.pathname === item.path
                ? "bg-blue-600 shadow-lg"
                : "hover:bg-slate-800"
            }`}
          >
            <span className="text-lg">{item.icon}</span>
            <span className="font-medium">{item.name}</span>
          </Link>
        ))}

      </nav>

      <div className="absolute bottom-6 left-6 right-6">
        <div className="bg-slate-800 rounded-xl p-4 text-center">
          <p className="text-xs text-slate-400">
            TransitOps v1.0
          </p>

          <p className="text-green-400 text-sm mt-1">
            ● System Online
          </p>
        </div>
      </div>

    </aside>
  );
}

export default Sidebar;