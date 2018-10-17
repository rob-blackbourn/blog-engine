import React, { Component, Fragment } from "react"
import CssBaseline from "@material-ui/core/CssBaseline"
import Main from "./components/main"

class App extends Component {
  render() {
    return (
      <Fragment>
        <CssBaseline />
        <Main />
      </Fragment>
    )
  }
}

export default App
