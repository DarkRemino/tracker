import {useState} from 'react'
import styles from '../style/track.module.css'
import { useNavigate } from 'react-router-dom';

let nav = useNavigate();
const resultRedirect = () => {
    let path = '/result';
    nav(path);
}

const Track = () => {

    return (
            <form action="submit" className='container'>

                <input type="text" name="track_number" id="track_number" placeholder='Tracking number' />
                <h3 className='clickable'>
                    <button type="submit" onMouseDown={resultRedirect}>Submit</button>
                </h3>                

            </form>
    );

}

export default Track;