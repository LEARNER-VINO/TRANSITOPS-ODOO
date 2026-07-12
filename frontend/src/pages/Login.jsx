import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const handleLogin = (e) => {
  e.preventDefault();

  navigate("/dashboard");
};

  return (
    <div className="login-container">
      {/* Left Side */}
      <div className="left-panel">
        <h1>TransitOps</h1>

        <p>Intelligent Operations Platform</p>

        <ul>
          <li>🚚 Trip Management</li>
          <li>🛵 Fleet Tracking</li>
          <li>👨‍✈️ Driver Safety</li>
          <li>📊 Predictive Analytics</li>
        </ul>
      </div>

      {/* Right Side */}
      <div className="right-panel">
        <form className="login-box" onSubmit={handleLogin}>
          <h2>Sign In</h2>

          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button type="submit">Sign In</button>
        </form>
      </div>
    </div>
  );
}

export default Login;