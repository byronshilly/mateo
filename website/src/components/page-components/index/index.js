import React from "react";
import { Link } from "gatsby";

import './style.scss';



const Index = () => {
    return (
        <>
            <h1>Home page</h1>
            <Link to='/login/'>Login</Link>
        </>
    );
};

export default Index;
