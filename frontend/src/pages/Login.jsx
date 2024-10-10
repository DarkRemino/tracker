import {useState} from 'react'
import styles from '../style/login.module.css'

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
            <form className='container' onSubmit={handleSubmit}>
                <input type='text' placeholder='Username' onChange={handleUsernameChange} />
                <input type='password' placeholder='Password' onChange={handlePasswordChange} />
                <h3 className='clickable'>
                    <button type='submit'>Login</button>
                </h3>

            </form>
    );
}

export default Login;