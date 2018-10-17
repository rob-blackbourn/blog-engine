import React, { Component } from "react"
import { withStyles } from "@material-ui/core/styles"

const styles = theme => ({})

class UnauthenticatedContent extends Component {
  render() {
    return <div>Unauthenticated content</div>
  }
}

export default withStyles(styles)(UnauthenticatedContent)
