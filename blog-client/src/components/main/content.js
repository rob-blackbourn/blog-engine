import React, { Component } from "react"
import PropTypes from "prop-types"
import { withStyles } from "@material-ui/core/styles"
import Authenticate from "../authentication/authenticate"
import UnauthenticatedContent from "./unauthenticated-content"
import AuthenticatedContent from "./authenticated-content"
import Grid from "@material-ui/core/Grid"

const styles = theme => ({})

class Content extends Component {
  render() {
    const { contentMode, onAuthenticated } = this.props

    switch (contentMode) {
      case "authenticated": {
        const { token, currentUser } = this.props
        return <AuthenticatedContent token={token} currentUser={currentUser} />
      }
      case "authenticating":
        return (
          <Grid container justify="center">
            <Authenticate onAuthenticated={onAuthenticated} />
          </Grid>
        )
      default:
        return <UnauthenticatedContent />
    }
  }
}

Content.propTypes = {
  classes: PropTypes.object.isRequired,
  contentMode: PropTypes.string.isRequired,
  onAuthenticated: PropTypes.func.isRequired,
  token: PropTypes.string,
  currentUser: PropTypes.object
}

export default withStyles(styles)(Content)
