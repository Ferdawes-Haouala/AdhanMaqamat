import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
    return (
    <nav className="navbar">
        <Link to="/" className="nav-link">Home</Link>
        <Link to="/maqamat" className="nav-link">Maqamat</Link>
        <Link to="/book-call" className="nav-link">Book a Call</Link>
        <Link to="/login" className="nav-link">Login</Link>
        <Link to="/register" className="nav-link">Register</Link>
    </nav>
);
}

export default Navbar;
