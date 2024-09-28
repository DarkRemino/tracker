import React from "react";
import styles from '../style/Landing.module.css';

const Landing = () => {
    return (
        <div className='container'>
            <h1 className={styles.landingHeading}>Welcome to Fryon's Tracker!</h1>
            <p className={styles.landingParagraph}>This app is still under development!
                If you'd like to follow its progress, you can check out the <a href='https://github.com/DarkRemino/tracker'>GitHub repository</a>.
            </p>
        </div>
    );
};

export default Landing;