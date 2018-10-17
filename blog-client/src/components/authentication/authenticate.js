import React, { Component } from "react"
import PropTypes from "prop-types"
import { withStyles } from "@material-ui/core/styles"
import Login from "./login"
import Register from "./register"
import { currentUser } from "../../api/user"

const styles = theme => ({
  container: {}
})

class Authenticate extends Component {
  state = {
    mode: "login"
  }

  handleToken = (token, onAuthenticated) => {
    currentUser(token, error => this.setState(error), onAuthenticated)
  }

  render() {
    const { onAuthenticated, classes } = this.props
    const { mode } = this.state

    if (mode === "login") {
      return (
        <Login
          className={classes.container}
          onToken={token => this.handleToken(token, onAuthenticated)}
          onModeChanged={mode => this.setState({ mode })}
        />
      )
    } else {
      return (
        <Register
          className={classes.container}
          onToken={token => this.handleToken(token, onAuthenticated)}
          onModeChanged={mode => this.setState({ mode })}
        />
      )
    }
  }
}

Authenticate.propTypes = {
  classes: PropTypes.object,
  onAuthenticated: PropTypes.func.isRequired
}

export default withStyles(styles)(Authenticate)
