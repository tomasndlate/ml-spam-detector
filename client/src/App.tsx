// import { useState } from 'react'
import './App.css'
import Navbar from './components/Navbar'
import Hero from './components/Hero';
import SpamDetector from './components/SpamDetector';

function App() {
  return (
    <>
      <Navbar />
      <Hero />
      <SpamDetector />
    </>
  )
}

export default App
