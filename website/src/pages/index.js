import React from "react";
import { Link } from "gatsby";

import Layout from "../components/layouts/layout";
import Image from "../components/common/image";
import SEO from "../components/common/seo";

import Index from "../components/page-components/index";



const IndexPage = () => {
    return(
        <Layout>
            <SEO title="Home" />

            <Index />
        </Layout>
    );
};

export default IndexPage;
