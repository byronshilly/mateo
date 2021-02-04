import React from "react";

import Layout from "../components/layouts/layout";
import SEO from "../components/common/SEO";

import Login from "../components/page-components/login";



const LoginPage = () => {
    return (
        <Layout>
            <SEO title="Login" />

            <Login />
        </Layout>
    );
};

export default LoginPage;
