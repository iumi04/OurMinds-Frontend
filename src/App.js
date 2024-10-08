import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar/SideBar.js';
import Today from "./components/Today/Today.js"
// import Prompts from './components/Prompts/Prompts';
// import Calendar from './components/Calendar/Calendar'; uncomment when bringing back pages <-- Umi
import Login from "./components/Login/Login.js";

function App() {
  return (
    <div className="App">
      <div className="container-fluid">
        <div className="row">
          <Router>
            <div className="col-md-3 p-0">
              <Sidebar />
            </div>
            <div className="col-md-9 good-evening">
              <Routes>
                <Route path="/" element={<Today />} />
                {/* uncomment when bringing back pages - Umi
                <Route path="/calendar" element={<Calendar />} />
                <Route path="/prompt" element={<Prompts />} /> */}
                <Route path="/login" element={<Login />} />
              </Routes>
            </div>
          </Router>
        </div>
      </div>
    </div>
  );
}

export default App;
