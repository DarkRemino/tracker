import {useState} from 'react'

const Login = () => {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleSubmit = (e) => {
        e.preventDefault()
        if (username === '' && password === '') {
            alert('Please fill in all fields!')
        } 
    }                                   

    const handleUsernameChange = (e) => {
        setUsername(e.target.value)
    }

    const handlePasswordChange = (e) => {
        setPassword(e.target.value)
    }

    return (
        <div class='container'>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <input type='text' placeholder='Username' onChange={handleUsernameChange} />
                <input type='password' placeholder='Password' onChange={handlePasswordChange} />
                <button type='submit'>Login</button>s
            </form>
        </div>
    );
}