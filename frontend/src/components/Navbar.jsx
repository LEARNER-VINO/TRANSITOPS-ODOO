import { FaBell, FaUserCircle } from "react-icons/fa";

function Navbar() {
  return (
    <header className="bg-white h-16 shadow flex justify-between items-center px-8">

      <div>
        <h2 className="text-2xl font-bold">
          Welcome 👋
        </h2>

        <p className="text-gray-500 text-sm">
          TransitOps Fleet Dashboard
        </p>
      </div>

      <div className="flex items-center gap-5">

        <input
          placeholder="Search..."
          className="border rounded-lg px-4 py-2 w-64"
        />

        <FaBell className="text-xl cursor-pointer" />

        <FaUserCircle className="text-4xl text-blue-600" />

      </div>

    </header>
  );
}

export default Navbar;