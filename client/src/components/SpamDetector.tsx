import React, { useState } from 'react'
import axios from 'axios'
import { IoIosInformationCircleOutline } from "react-icons/io";

function SpamDetector() {

    const [text, setText] = useState('')
    const [prediction, setPrediction] = useState('')
    // For loading handling
    const [loading, setLoading] = useState(false);

    const handleText = (event: React.ChangeEvent<HTMLTextAreaElement>): void => {
        setText(event.target.value as string);
    }

    function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault() // prevent the default form submission
        setLoading(true);  // Start loading
        axios.post('http://127.0.0.1:3000/predict', { "text": text })
        .then(response => {
            setPrediction(response.data.prediction)
        }).catch(err => {
            console.log(err);
        }).finally(() => {
            setLoading(false);
        });
    }

  return (
    <div className='w-full h-fit px-6 flex justify-center items-center'>
        <div className='w-full max-w-7xl md:min-h-110 min-h-150 rounded-lg border-1 border-zinc-300 p-5 grid gap-2 md:grid-cols-[1fr_300px] grid-cols-1 grid-rows-1'>
            <div className='h-full grid grid-rows-[auto_1fr] rounded-lg gap-2 overflow-hidden'>
                <div className='w-full h-full flex flex-initial items-center p-5 bg-neutral-100 gap-2 text-sm'>
                    <IoIosInformationCircleOutline className='text-neutral-700 md:text-sm text-xl' />
                    <p className='text-neutral-700'>Please enter the text you want to check for spam in the inout below.</p>
                </div>
                <form onSubmit={handleSubmit} className='w-full h-full grid grid-rows-[auto_1fr_auto] gap-2'>
                    <label htmlFor='text' className='font-medium b'>Text to detect spam:</label>
                    <textarea id='text' name="text" onChange={handleText} 
                    placeholder='Is this a spam or not...' 
                    className='w-full h-full p-1 resize-none bg-neutral-50 rounded-lg focus:outline-none focus:border-none' />
                    <div className='flex justify-end'>
                        <button className='inline-block w-fit px-6 py-3 rounded-md bg-zinc-950 text-white hover:cursor-pointer'>Detect Spam</button>
                    </div>
                </form>
            </div>
            <div className='h-fit'>
                <p>Result: {loading ? 'loading...' : prediction}</p>
            </div>
        </div>
    </div>
  )
}

export default SpamDetector