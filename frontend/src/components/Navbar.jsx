import { FaBell } from "react-icons/fa";

function Navbar() {
  return (
    <header className="h-16 bg-white shadow-sm border-b flex items-center justify-between px-8 sticky top-0 z-20">
      <div>
        <h1 className="text-2xl font-bold text-gray-800">
          Dashboard
        </h1>
        <p className="text-sm text-gray-500">
          Welcome back to TransitOps
        </p>
      </div>

      <div className="flex items-center gap-5">
        <input
          type="text"
          placeholder="Search..."
          className="w-72 border rounded-lg px-4 py-2 outline-none focus:ring-2 focus:ring-blue-500"
        />

        <FaBell className="text-xl text-gray-600 cursor-pointer hover:text-blue-600" />

        <img
          src="https://i.pravatar.cc/45"
          alt="Profile"
          className="w-11 h-11 rounded-full border"
        />
      </div>
    </header>
  );
}

export default Navbar;