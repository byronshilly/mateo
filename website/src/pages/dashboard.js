import React from "react";
import { Link } from "gatsby";

import Layout from "../components/layouts/layout";
import Image from "../components/common/image";
import SEO from "../components/common/seo";

import Dashboard from "../components/page-components/dashboard";



const IndexPage = () => {
    return(
        <Layout>
            <SEO title="Dashboard" />

            <Dashboard />
        </Layout>
    );
};

export default IndexPage;
