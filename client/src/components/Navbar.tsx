// import React from 'react'
import { FaGithub } from "react-icons/fa";
import { FaLinkedin } from "react-icons/fa";

function Navbar() {
  return (
    <>
    <nav className='w-full h-20 bg-white-950 flex px-5 text-black justify-between items-center'>
      <h1 className='text-lg font-bold'>ML Spam Detector</h1>
      <div className='flex gap-2 text-2xl'>
        <a href="https://github.com/tomasndlate" target="_blank" rel="noopener noreferrer">
          <FaGithub />
        </a>
        <a href="https://www.linkedin.com/in/tomasndlate/" target="_blank" rel="noopener noreferrer">
          <FaLinkedin />
        </a>
      </div>
    </nav>
    </>
  )
}

export default Navbar