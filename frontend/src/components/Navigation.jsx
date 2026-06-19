import React from 'react'
import { Link } from 'react-router-dom'
import './Navigation.css'

function Navigation() {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-brand">
          Smart Campus Assistant
        </Link>
        <ul className="nav-menu">
          <li className="nav-item">
            <Link to="/" className="nav-link">
              Dashboard
            </Link>
          </li>
          <li className="nav-item">
            <a href="#students" className="nav-link">
              Students
            </a>
          </li>
          <li className="nav-item">
            <a href="#attendance" className="nav-link">
              Attendance
            </a>
          </li>
          <li className="nav-item">
            <a href="#courses" className="nav-link">
              Courses
            </a>
          </li>
        </ul>
      </div>
    </nav>
  )
}

export default Navigation
