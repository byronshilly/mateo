import React, { useState, useEffect, useRef } from "react";
import { Link, navigate } from "gatsby";
import { Router } from "@reach/router"

import { AuthApi, UserApi } from "../../../utilities/api.js";

import './style.scss';



const Dashboard = () => {
    const [user, setUser] = useState({'id': null});
    const [accessToken, setAccessToken] = useState("");
    const [refreshToken, setRefreshToken] = useState(localStorage.getItem("refreshToken"));

    const authService = useRef();
    const userService = useRef();

    /** 
     * If the access CSRF token is gone, we need to refresh the user's token. 
     */
    if (!accessToken) {
        /** 
         * Redirect users to login if they aren't authenticated.
         */
        if (!refreshToken) {
            navigate('/login');
        }

        authService.current = new AuthApi();
        authService.current.refreshCsrfToken = refreshToken;
        authService.current.refresh()
            .then((response) => {
                if (response.refresh) {
                    setAccessToken(response['access_csrf_token']);
                } else {
                    navigate('/login');
                }
            });
    }



    
	return(
        <>
            <nav>
                <Link to='/dashboard'>Home</Link><br />
                <Link to='/dashboard/account'>Account</Link>
            </nav>

            <Router basepath='/dashboard'>
                <Home path='/' />
                <Account path='/account' />
            </Router> 
        </>
	);
};

const Home = () => {
    const logoutUser = () => {
        let authService = new AuthApi(); 
        authService.logout()
            .then((response) => {
                if (response.logout) {
                    navigate('/login');
                }
            });
    }

    return (
        <>
            <h1>Dash home</h1>
            <button onClick={logoutUser}>Logout</button>
        </>
    );
}

const Account = () => {
    return(
        <>
            <h1>Account</h1>
        </>
    )
}

export default Dashboard;
