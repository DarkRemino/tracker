import React from 'react'

const Navbar = () => {
    return (
        <nav>
            <div className='navbar-left'>
                <h3 className='clickable'>Tracker v0.1.0</h3>
            </div>

            <div className='navbar-center'>
                <ul>
                    <li className='clickable'><a href='/'>Home</a></li>
                    <li className='clickable'><a href='/about'>About</a></li>
                    <li className='clickable'><a href='/contact'>Contact</a></li>
                </ul>
            </div>

            <div className='navbar-right'>
                <h3 className='clickable'><a href="/login">Login</a></h3>
            </div>
        </nav>
    );
};

export default Navbar;