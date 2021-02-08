import React, { useEffect } from "react";

import { AuthApi, UserApi } from "../../../utilities/api.js"

import './style.scss';


const Login = () => {
    useEffect(() => {
        let authApi = new AuthApi();
    });
    
    return(
        <>
            <h1>Login</h1>
            <form className="login-form row no-gutters">
                <label className="col-12" htmlFor="username">Username:</label>
                <input className="col-12" type="text" name="username" required></input>

                <label className="col-12" htmlFor="password">Password:</label>
                <input className="col-12" type="password" name="password" required></input>
            </form>
        </>
    );
};

export default Login;
