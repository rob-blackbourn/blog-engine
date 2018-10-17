import React, { Component } from "react"
import PropTypes from "prop-types"
import { withStyles } from "@material-ui/core/styles"
import Grid from "@material-ui/core/Grid"
import TextField from "@material-ui/core/TextField"
import Button from "@material-ui/core/Button"
import MultiLineTextField from "../core/multi-line-text-field"
import { register } from "../../api/authentication"

const styles = theme => ({
  container: {
    width: 350
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

class Register extends Component {
  state = {
    primaryEmail: "",
    password: "",
    secondaryEmails: [""],
    givenNames: [""],
    familyName: "",
    nickname: ""
  }

  handleClick = onToken => {
    const {
      primaryEmail,
      password,
      secondaryEmails,
      givenNames,
      familyName,
      nickname
    } = this.state

    register(
      primaryEmail,
      password,
      secondaryEmails,
      givenNames,
      familyName,
      nickname,
      error => this.setState({ error }),
      onToken
    )
  }

  render() {
    const { onToken, onModeChanged, classes } = this.props
    const {
      primaryEmail,
      password,
      secondaryEmails,
      givenNames,
      familyName,
      nickname
    } = this.state

    return (
      <Grid container className={classes.container}>
        <Grid item xs={12}>
          <TextField
            label="Email"
            className={classes.textField}
            value={primaryEmail}
            margin="normal"
            onChange={event =>
              this.setState({ primaryEmail: event.target.value })
            }
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
        <Grid item xs={12}>
          <MultiLineTextField
            className={classes.textField}
            label="Secondary Email"
            lines={secondaryEmails}
            onChange={lines => this.setState({ secondaryEmails: lines })}
          />
        </Grid>
        <Grid item xs={12}>
          <MultiLineTextField
            className={classes.textField}
            label="Given Name"
            lines={givenNames}
            onChange={lines => this.setState({ givenNames: lines })}
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            label="Family Name"
            className={classes.textField}
            value={familyName}
            margin="normal"
            onChange={event =>
              this.setState({ familyName: event.target.value })
            }
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            label="Nickname"
            className={classes.textField}
            value={nickname}
            margin="normal"
            onChange={event => this.setState({ nickname: event.target.value })}
          />
        </Grid>
        <Grid container>
          <Grid item xs={6}>
            <Button
              variant="text"
              color="primary"
              className={classes.button}
              onClick={() => onModeChanged("login")}
            >
              Login
            </Button>
          </Grid>
          <Grid item xs={6}>
            <Button
              variant="contained"
              color="primary"
              className={classes.button}
              onClick={() => this.handleClick(onToken)}
            >
              Register
            </Button>
          </Grid>
        </Grid>
      </Grid>
    )
  }
}

Register.propTypes = {
  classes: PropTypes.object,
  onToken: PropTypes.func.isRequired,
  onModeChanged: PropTypes.func.isRequired
}

export default withStyles(styles)(Register)
