/**
 * Layout component that queries for data
 * with Gatsby's useStaticQuery component
 *
 * See: https://www.gatsbyjs.com/docs/use-static-query/
 */

import React from "react"
import PropTypes from "prop-types"
import { graphql } from "gatsby"

import "./layout.css"

const Layout = ({ children }) => {

    return (
        <>{children}</>
    )
};

Layout.propTypes = {
    children: PropTypes.node.isRequired,
};

export default Layout;

// Not needed at the moment
// export const data = graphql`
//     query SiteTitleQuery {
//         site {
//             siteMetadata {
//                 title
//             }
//         }
//     }
// `;
