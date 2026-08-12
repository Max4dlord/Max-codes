import { Link, NavLink, useLocation } from 'react-router-dom'
import { useEffect, useState } from 'react'
import { loadSession } from '../progress.js'

export default function Navbar() {
  const loc = useLocation()
  const [hasSession, setHasSession] = useState(() => !!loadSession())

  useEffect(() => {
    setHasSession(!!loadSession())
  }, [loc.pathname])

  return (
    <header className="nav">
      <Link to="/" className="nav-brand">
        <span className="nav-logo">∑</span>
        <span className="nav-title">MTH&nbsp;202 · <em>CBT Lab</em></span>
      </Link>
      <nav className="nav-links">
        <NavLink to="/" end>Home</NavLink>
        <NavLink to="/dashboard">Dashboard</NavLink>
        {hasSession && (
          <NavLink to="/test" className="nav-resume">Resume test →</NavLink>
        )}
      </nav>
    </header>
  )
}
