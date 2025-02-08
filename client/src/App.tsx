import Navbar from './components/Navbar'
import Hero from './components/Hero';
import SpamDetector from './components/SpamDetector';

function App() {
  return (
    <>
      <Navbar />
      <Hero />
      <div className='my-10'>
        <SpamDetector />
      </div>
    </>
  )
}

export default App
