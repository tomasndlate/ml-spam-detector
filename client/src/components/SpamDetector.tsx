import React, { useState } from 'react'
import axios from 'axios'

function SpamDetector() {

    const [text, setText] = useState('')

    // interface TextEvent extends React.ChangeEvent<HTMLTextAreaElement> {
    //     text: string;
    // }

    const handleText = (event: React.ChangeEvent<HTMLTextAreaElement>): void => {
        setText(event.target.value as string);
    }
    function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault()
        axios.post('http://127.0.0.1:3000/predict',
            { "text": text }
        ).then(response => {
            console.log(response.data)
        }).catch(err => console.log(err))
    }

  return (
    <>
    <form onSubmit={handleSubmit}>
        <textarea name="text" onChange={handleText} placeholder='text here' />
        <button>Detect</button>
    </form>
    <p>Result: </p>
    </>
  )
}

export default SpamDetector