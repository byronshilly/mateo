import React, { useEffect } from "react";
import wretch from "wretch";

import './style.scss';


const Login = () => {

    useEffect(() => {
        wretch("http://localhost:5000/auth")
            .post({"username":"byron", "password":"Narutovpain1?"})
            .json(response => {
                let token = response.access_token;
                wretch("http://localhost:5000/api/v1/user/b59574aa-47f4-484a-9924-5a5a86549055")
                    .auth(`JWT ${ token }`)
                    .get()
                    .res(response => {
                        console.log(response);
                    });
            });

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
