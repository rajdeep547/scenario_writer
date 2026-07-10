import { NavLink, Outlet } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './Layout.css';

export default function Layout() {
  const { user, logout } = useAuth();

  return (
    <div className="layout">
      <header className="header glass">
        <div className="header-brand">
          <span className="brand-icon">🎯</span>
          <h1>AI Scenario Writer</h1>
        </div>
        <nav className="header-nav">
          <NavLink to="/" end className={({ isActive }) => (isActive ? 'nav-link active' : 'nav-link')}>
            Generate
          </NavLink>
          <NavLink to="/history" className={({ isActive }) => (isActive ? 'nav-link active' : 'nav-link')}>
            History
          </NavLink>
        </nav>
        <div className="header-user">
          <span className="username">{user?.username}</span>
          <button className="btn btn-ghost" onClick={logout}>
            Logout
          </button>
        </div>
      </header>
      <main className="main-content">
        <Outlet />
      </main>
    </div>
  );
}
