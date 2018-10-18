import React, { Component } from "react"
import PropTypes from "prop-types"
import { withStyles } from "@material-ui/core/styles"
import Grid from "@material-ui/core/Grid"
import TextField from "@material-ui/core/TextField"
import Button from "@material-ui/core/Button"
import MultiLineTextField from "../core/multi-line-text-field"
import { updateProfile } from "../../api/authentication"

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

class Profile extends Component {
  constructor(props) {
    super(props)

    const {
      primaryEmail,
      secondaryEmails,
      givenNames,
      familyName,
      nickname
    } = this.props.currentUser

    this.state = {
      originalPrimaryEmail: primaryEmail,
      primaryEmail,
      secondaryEmails,
      givenNames,
      familyName,
      nickname
    }
  }

  handleUpdate = () => {
    const {
      originalPrimaryEmail,
      primaryEmail,
      password,
      secondaryEmails,
      givenNames,
      familyName,
      nickname
    } = this.state

    updateProfile(
      originalPrimaryEmail,
      primaryEmail,
      password,
      secondaryEmails,
      givenNames,
      familyName,
      nickname,
      error => this.setState({ error }),
      currentUser => this.props.onUpdated(currentUser)
    )
  }

  render() {
    const { onUpdated, classes } = this.props
    const {
      primaryEmail,
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
              variant="contained"
              color="primary"
              className={classes.button}
              onClick={this.handleClick}
            >
              Register
            </Button>
          </Grid>
        </Grid>
      </Grid>
    )
  }
}

Profile.propTypes = {
  classes: PropTypes.object,
  onUpdated: PropTypes.func.isRequired,
  currentUser: PropTypes.object.isRequired
}

export default withStyles(styles)(Profile)
