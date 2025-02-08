// import React from 'react'

function Hero() {
  return (
    <div className='px-10 flex flex-col gap-4 text-white text-left py-35 bg-radial-[at_70%_75%] from-teal-500 via-emerald-500 to-teal-500 to-90%'>
        <a href="https://github.com/tomasndlate/ml-spam-detector" target="_blank" rel="noopener noreferrer" 
          className='inline-block w-fit px-6 py-3 rounded-md bg-zinc-950'>Project Documentation</a>
        <h1 className='text-4xl font-bold'>Machine Learning Spam Detector</h1>
        <p>Machine Learning project to detect spam content. Using a serverless architecture, powered by AWS services Lambda and API Gateway.</p>
    </div>
  )
}

export default Hero