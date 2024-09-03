import  React from 'react'

const NotFound = () => {
    return (
        <div className="container">
            <h1>Uh oh! This page doesn't exist. 🤖</h1>
            <p>There is no page at this address. You can return <a href="/">home</a> or <a href="/register">login</a>. <br />
            If you think there should be a page here, please <a href="https://github.com/DarkRemino/tracker/issues">open an issue</a>.</p>
        </div>
    );
};

export default NotFound;