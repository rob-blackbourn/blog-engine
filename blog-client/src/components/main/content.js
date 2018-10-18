import React, { Component } from "react"
import PropTypes from "prop-types"
import { withStyles } from "@material-ui/core/styles"
import Grid from "@material-ui/core/Grid"
import Authenticate from "../authentication/authenticate"
import UnauthenticatedContent from "./unauthenticated-content"
import AuthenticatedContent from "./authenticated-content"
import Profile from "../authentication/profile"

const styles = theme => ({})

class Content extends Component {
  render() {
    const {
      contentMode,
      onAuthenticated,
      onProfileChanged,
      currentUser
    } = this.props

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
      case "profile":
        return (
          <Grid container justify="center">
            <Profile currentUser={currentUser} onUpdated={onProfileChanged} />
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
  onProfileChanged: PropTypes.func.isRequired,
  token: PropTypes.string,
  currentUser: PropTypes.object
}

export default withStyles(styles)(Content)
