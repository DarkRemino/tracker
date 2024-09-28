import React from 'react'
import styles from '../style/Navbar.module.css';

const Navbar = () => {
    return (
        <nav>
            <div className={styles.navbarLeft}>
                <h3 className={styles.clickable}>Tracker v0.1.0</h3>
            </div>

            <div className={styles.navbarCenter}>
                <ul>
                    <li className={styles.clickable}><a href='/'>Home</a></li>
                    <li className={styles.clickable}><a href='/about'>About</a></li>
                    <li className={styles.clickable}><a href='/contact'>Contact</a></li>
                </ul>
            </div>

            <div className={styles.navbarRight}>
                <h3 className={styles.clickable}>Login</h3>
            </div>
        </nav>
    );
};

export default Navbar;