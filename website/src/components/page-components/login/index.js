import React, { useState, useRef } from "react";
import { navigate } from "gatsby";

import { AuthApi, UserApi } from "../../../utilities/api.js"

import './style.scss';


const Login = () => {
    const authService = useRef();
    const [refreshToken, setRefreshToken] = useState(localStorage.getItem("refreshToken"));

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const [message, setMessage] = useState(null);

    /**
     * See if the user is already authenticated.
     */
    if (refreshToken) {
        if (!authService.current) {
            authService.current = new AuthApi();
        }

        authService.current.refreshCsrfToken = refreshToken;
        authService.current.refresh()
            .then((response) => {
                if (response.refresh) {
                    navigate('/dashboard');
                } else {
                    setRefreshToken("");
                }
            });
    }

    /**
     * Form handlers
     */
    const handleUsernameInput = (event) => {
        setUsername(event.target.value); 
    }

    const handlePasswordInput = (event) => {
        setPassword(event.target.value);
    }

    const loginUser = (event) => {
        if (!authService.current) {
            authService.current = new AuthApi();
        }

        authService.current.login(username, password)
            .then((response) => {
                if (response.login) {
                    localStorage.setItem('refreshToken', response['refresh_csrf_token']);
                    navigate('/dashboard');
                } else {
                    setMessage("Your username or password is incorrect.");
                }
            });

        event.preventDefault();
    }
    
    return(
        <>
            <div> 
                <h1>Login</h1>

                <form className="login-form row no-gutters" onSubmit={loginUser}>
                    <label className="col-12">Username:</label>
                    <input className="col-12" type="text" name="username" onChange={handleUsernameInput} required />

                    <label className="col-12">Password:</label>
                    <input className="col-12" type="password" name="password" onChange={handlePasswordInput} required />

                    <input type="submit" value="submit" />
                </form>

                { message && <div className="alert alert-danger">{message}</div> }
            </div>
        </>
    );
};

export default Login;
