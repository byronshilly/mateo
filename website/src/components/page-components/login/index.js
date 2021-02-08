import React, { useEffect } from "react";

import { AuthApi } from "../../../utilities/api.js"

import './style.scss';


const Login = () => {

    useEffect(() => {
        let api = new AuthApi();
        let result = api.login("byron", "PASSWORD");
        console.log(result);
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
