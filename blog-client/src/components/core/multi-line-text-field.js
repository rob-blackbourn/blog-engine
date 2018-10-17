import React, { Component } from "react"
import PropTypes from "prop-types"
import { withStyles } from "@material-ui/core/styles"
import TextField from "@material-ui/core/TextField"
import Button from "@material-ui/core/Button"
import ListEditor from "./list-editor"

const styles = theme => ({
  textField: {
    marginLeft: theme.spacing.unit,
    marginRight: theme.spacing.unit,
    width: 300
  },
  buttons: {
    width: 50
  },
  button: {}
})

class MultiLineTextField extends Component {
  render() {
    const {
      classes,
      lines,
      onChange,
      label,
      addLabel,
      removeLabel
    } = this.props

    return (
      <ListEditor
        list={lines}
        onChange={onChange}
        defaultValue=""
        itemRenderer={(item, index, list, onValueChange) => (
          <TextField
            className={classes.textField}
            label={label}
            value={item}
            key={index}
            margin="normal"
            onChange={onValueChange}
          />
        )}
        addRenderer={(item, index, list, onAdd) => (
          <Button onClick={onAdd}>{addLabel}</Button>
        )}
        removeRenderer={(item, index, list, onRemove) => (
          <Button onClick={onRemove} className={classes.button}>
            {removeLabel}
          </Button>
        )}
      />
    )
  }
}

MultiLineTextField.propTypes = {
  classes: PropTypes.object,
  lines: PropTypes.arrayOf(PropTypes.string).isRequired,
  onChange: PropTypes.func.isRequired,
  label: PropTypes.string.isRequired,
  addLabel: PropTypes.any.isRequired,
  removeLabel: PropTypes.any.isRequired
}

MultiLineTextField.defaultProps = {
  addLabel: "Add",
  removeLabel: "Remove"
}
export default withStyles(styles)(MultiLineTextField)
