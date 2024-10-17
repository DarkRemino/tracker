import { useState } from 'react'
import styles from '../style/login.module.css'

const Login = () => {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (username === '' && password === '') {
            alert('Please fill in all fields!');
        }

        try {
            const response = await fetch('http://127.0.0.1:8000/login', {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                },
                body: JSON.stringify({
                    username,
                    password
                })
            });

            const data = await response.json();

            if (response.ok) {
                alert('Login successful!');
            }
            else {
                alert(data.detail || 'Login failed!');
            }
        } catch (error) {
            console.error('Error during login:', error);
            alert('An error occured during login!');
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