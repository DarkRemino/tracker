import React from 'react'

const Navbar = () => {
    return (
        <nav>
            <div className='navbar-left'>
                <h3>Tracker v0.1</h3>
            </div>

            <div className='navbar-center'>
                <ul>
                    <li><a href='/'>Home</a></li>
                    <li><a href='/login'>About</a></li>
                    <li><a href='/register'>Contact</a></li>
                </ul>
            </div>

            <div className='navbar-right'>
                <h3>Login</h3>
            </div>
        </nav>
    );
};

export default Navbar;