import {
  FaHome,
  FaTruck,
  FaRoute,
  FaChartLine,
  FaUserTie,
  FaCog,
} from "react-icons/fa";

const menu = [
  { icon: <FaHome />, text: "Dashboard" },
  { icon: <FaTruck />, text: "Vehicles" },
  { icon: <FaRoute />, text: "Trips" },
  { icon: <FaUserTie />, text: "Drivers" },
  { icon: <FaChartLine />, text: "Analytics" },
  { icon: <FaCog />, text: "Settings" },
];

function Sidebar() {
  return (
    <aside className="fixed left-0 top-0 w-64 h-screen bg-slate-900 text-white">
      <div className="text-3xl font-bold p-6 border-b border-slate-700">
        TransitOps
      </div>

      <nav className="mt-6">
        {menu.map((item) => (
          <button
            key={item.text}
            className="w-full flex items-center gap-4 px-6 py-4 hover:bg-slate-800 transition text-left"
          >
            {item.icon}
            {item.text}
          </button>
        ))}
      </nav>
    </aside>
  );
}

export default Sidebar;