import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './style/_main.css'
import Landing from './pages/Landing'
import Login from './pages/Login'
import Track from './pages/Track'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import NotFound from './pages/404'

function App() {
  return (
    <>
      <Router>
        <Navbar />
          <Routes>
            <Route path='/' element={<Landing />} />
            <Route path='/track' element={<Track />}/>
            <Route path='/login' element={<Login/>} />
            <Route path='*' element={<NotFound />} />
          </Routes>
        <Footer />
      </Router>
    </>
  )
}

export default App
