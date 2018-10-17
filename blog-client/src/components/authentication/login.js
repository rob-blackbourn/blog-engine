import React, { Component } from "react"
import PropTypes from "prop-types"
import { withStyles } from "@material-ui/core/styles"
import Grid from "@material-ui/core/Grid"
import TextField from "@material-ui/core/TextField"
import Button from "@material-ui/core/Button"
import Dialog from "@material-ui/core/Dialog"
import DialogTitle from "@material-ui/core/DialogTitle"
import DialogActions from "@material-ui/core/DialogActions"
import DialogContent from "@material-ui/core/DialogContent"
import DialogContentText from "@material-ui/core/DialogContentText"
import { login } from "../../api/authentication"

const styles = theme => ({
  container: {
    width: 450
  },
  textField: {
    marginLeft: theme.spacing.unit,
    marginRight: theme.spacing.unit,
    width: 300
  },
  button: {
    margin: theme.spacing.unit
  }
})

class Login extends Component {
  state = {
    email: "",
    password: "",
    error: null
  }

  handleClick = onToken => {
    const { email, password } = this.state

    login(email, password, error => this.setState({ error }), onToken)
  }

  render() {
    const { onToken, onModeChanged, classes } = this.props
    const { error, email, password } = this.state

    if (error) {
      return (
        <Dialog
          open={error !== null}
          onClose={() => this.setState({ error: null })}
        >
          <DialogTitle>Login failed</DialogTitle>
          <DialogContent>
            <DialogContentText>{error}</DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button
              onClick={() => this.setState({ error: null })}
              color="primary"
            >
              Dismiss
            </Button>
          </DialogActions>
        </Dialog>
      )
    }
    return (
      <Grid container className={classes.container}>
        <Grid item xs={12}>
          <TextField
            label="Email"
            className={classes.textField}
            value={email}
            margin="normal"
            onChange={event => this.setState({ email: event.target.value })}
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            label="Password"
            type="password"
            className={classes.textField}
            value={password}
            margin="normal"
            onChange={event => this.setState({ password: event.target.value })}
          />
        </Grid>
        <Grid container>
          <Grid item xs={6}>
            <Button
              variant="text"
              color="primary"
              className={classes.button}
              onClick={() => onModeChanged("register")}
            >
              Register
            </Button>
          </Grid>
          <Grid item xs={6}>
            <Button
              variant="contained"
              color="primary"
              className={classes.button}
              onClick={() => this.handleClick(onToken)}
            >
              Login
            </Button>
          </Grid>
        </Grid>
      </Grid>
    )
  }
}

Login.propTypes = {
  classes: PropTypes.object,
  onToken: PropTypes.func.isRequired,
  onModeChanged: PropTypes.func.isRequired
}

export default withStyles(styles)(Login)
