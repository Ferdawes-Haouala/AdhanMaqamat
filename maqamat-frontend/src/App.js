import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import MaqamatList from './pages/MaqamatList';
import MaqamDetails from './pages/MaqamDetails';
import BookCall from './pages/BookCall';
import Login from './pages/Login';
import Register from './pages/Register';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/maqamat" element={<MaqamatList />} />
          <Route path="/maqamat/:id" element={<MaqamDetails />} />
          <Route path="/book-call" element={<BookCall />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
