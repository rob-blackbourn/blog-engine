import React from "react"
import PropTypes from "prop-types"
import classNames from "classnames"
import { withStyles } from "@material-ui/core/styles"
import Drawer from "@material-ui/core/Drawer"
import AppBar from "@material-ui/core/AppBar"
import Toolbar from "@material-ui/core/Toolbar"
import List from "@material-ui/core/List"
import Typography from "@material-ui/core/Typography"
import Divider from "@material-ui/core/Divider"
import IconButton from "@material-ui/core/IconButton"
import Badge from "@material-ui/core/Badge"
import MenuIcon from "@material-ui/icons/Menu"
import AccountCircle from "@material-ui/icons/AccountCircle"
import ChevronLeftIcon from "@material-ui/icons/ChevronLeft"
import NotificationsIcon from "@material-ui/icons/Notifications"
import Menu from "@material-ui/core/Menu"
import MenuItem from "@material-ui/core/MenuItem"

import { mainListItems, secondaryListItems } from "./list-items"
import Content from "./content"

const drawerWidth = 240

const styles = theme => ({
  root: {
    display: "flex"
  },
  toolbar: {
    paddingRight: 24 // keep right padding when drawer closed
  },
  toolbarIcon: {
    display: "flex",
    alignItems: "center",
    justifyContent: "flex-end",
    padding: "0 8px",
    ...theme.mixins.toolbar
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(["width", "margin"], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen
    })
  },
  appBarShift: {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(["width", "margin"], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen
    })
  },
  menuButton: {
    marginLeft: 12,
    marginRight: 36
  },
  menuButtonHidden: {
    display: "none"
  },
  title: {
    flexGrow: 1
  },
  drawerPaper: {
    position: "relative",
    whiteSpace: "nowrap",
    width: drawerWidth,
    transition: theme.transitions.create("width", {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen
    })
  },
  drawerPaperClose: {
    overflowX: "hidden",
    transition: theme.transitions.create("width", {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen
    }),
    width: theme.spacing.unit * 7,
    [theme.breakpoints.up("sm")]: {
      width: theme.spacing.unit * 9
    }
  },
  appBarSpacer: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    padding: theme.spacing.unit * 3,
    height: "100vh",
    overflow: "auto"
  },
  chartContainer: {
    marginLeft: -22
  },
  tableContainer: {
    height: 320
  },
  h5: {
    marginBottom: theme.spacing.unit * 2
  }
})

class Dashboard extends React.Component {
  state = {
    token: null,
    isDrawerOpen: true,
    userMenuAnchorEl: null,
    contentMode: "unauthenticated"
  }

  handleDrawerOpen = () => {
    this.setState({ isDrawerOpen: true })
  }

  handleDrawerClose = () => {
    this.setState({ isDrawerOpen: false })
  }

  openUserMenu = event => {
    this.setState({ userMenuAnchorEl: event.currentTarget })
  }

  closeUsermenu = () => {
    this.setState({ userMenuAnchorEl: null })
  }

  handleAuthenticationRequested = () => {
    this.setState({ userMenuAnchorEl: null, contentMode: "authenticating" })
  }

  handleAuthentication = (token, currentUser) => {
    const contentMode = token ? "authenticated" : "unauthenticated"
    this.setState({ token, currentUser, contentMode })
  }

  render() {
    const { classes } = this.props
    const {
      userMenuAnchorEl,
      isDrawerOpen,
      token,
      currentUser,
      contentMode
    } = this.state
    const isUserMenuOpen = Boolean(userMenuAnchorEl)
    const isAuthenticated = Boolean(token)

    return (
      <div className={classes.root}>
        <AppBar
          position="absolute"
          className={classNames(
            classes.appBar,
            isDrawerOpen && classes.appBarShift
          )}
        >
          <Toolbar disableGutters={!isDrawerOpen} className={classes.toolbar}>
            <IconButton
              color="inherit"
              aria-label="Open drawer"
              onClick={this.handleDrawerOpen}
              className={classNames(
                classes.menuButton,
                isDrawerOpen && classes.menuButtonHidden
              )}
            >
              <MenuIcon />
            </IconButton>
            <Typography
              component="h1"
              variant="h6"
              color="inherit"
              noWrap
              className={classes.title}
            >
              Dashboard
            </Typography>

            <IconButton color="inherit">
              <Badge badgeContent={4} color="secondary">
                <NotificationsIcon />
              </Badge>
            </IconButton>

            <div>
              <IconButton
                aria-owns={isUserMenuOpen ? "menu-appbar" : null}
                aria-haspopup="true"
                onClick={this.openUserMenu}
                color="inherit"
              >
                <AccountCircle />
              </IconButton>
              <Menu
                id="menu-appbar"
                anchorEl={userMenuAnchorEl}
                anchorOrigin={{
                  vertical: "top",
                  horizontal: "right"
                }}
                transformOrigin={{
                  vertical: "top",
                  horizontal: "right"
                }}
                open={isUserMenuOpen}
                onClose={this.closeUsermenu}
              >
                <MenuItem
                  onClick={this.handleAuthenticationRequested}
                  disabled={isAuthenticated}
                >
                  Login
                </MenuItem>
                <MenuItem
                  onClick={this.closeUsermenu}
                  disabled={!isAuthenticated}
                >
                  Profile
                </MenuItem>
                <MenuItem
                  onClick={this.closeUsermenu}
                  disabled={!isAuthenticated}
                >
                  My account
                </MenuItem>
              </Menu>
            </div>
          </Toolbar>
        </AppBar>
        <Drawer
          variant="permanent"
          classes={{
            paper: classNames(
              classes.drawerPaper,
              !isDrawerOpen && classes.drawerPaperClose
            )
          }}
          open={isDrawerOpen}
        >
          <div className={classes.toolbarIcon}>
            <IconButton onClick={this.handleDrawerClose}>
              <ChevronLeftIcon />
            </IconButton>
          </div>
          <Divider />
          <List>{mainListItems}</List>
          <Divider />
          <List>{secondaryListItems}</List>
        </Drawer>
        <main className={classes.content}>
          <div className={classes.appBarSpacer} />
          <Content
            contentMode={contentMode}
            onAuthenticated={this.handleAuthentication}
            token={token}
            currentUser={currentUser}
          />
        </main>
      </div>
    )
  }
}

Dashboard.propTypes = {
  classes: PropTypes.object.isRequired
}

export default withStyles(styles)(Dashboard)
