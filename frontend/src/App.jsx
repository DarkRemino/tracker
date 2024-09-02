import React from 'react'
import './style/_main.css'
import Landing from './pages/Landing'
import Navbar from './components/Navbar'
import Footer from './components/Footer'

function App() {
  return (
    <>
      <Navbar />
      <Landing />
      <Footer />
    </>
  )
}

export default App
