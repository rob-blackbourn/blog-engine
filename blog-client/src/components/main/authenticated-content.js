import React, { Component } from "react"
import PropTypes from "prop-types"
import { withStyles } from "@material-ui/core/styles"

const styles = theme => ({})

class AuthenticatedContent extends Component {
  render() {
    const { token, currentUser } = this.props

    return <div>Authenticated content for {currentUser.primaryEmail}</div>
  }
}

AuthenticatedContent.proptypes = {
  token: PropTypes.string.isRequired,
  currentUser: PropTypes.object.isRequired
}

export default withStyles(styles)(AuthenticatedContent)
