import React, { Fragment } from "react"
import PropTypes from "prop-types"
import { withStyles } from "@material-ui/core/styles"
import Grid from "@material-ui/core/Grid"

const styles = theme => ({})

const ListEditor = ({
  list,
  onChange,
  itemRenderer,
  addRenderer,
  removeRenderer,
  defaultValue
}) => (
  <Fragment>
    {(list || []).map((item, index) => (
      <Grid container key={index}>
        <Grid item xs={10}>
          {itemRenderer(item, index, list, event =>
            onChange([
              ...list.slice(0, index),
              event.target.value,
              ...list.slice(index + 1)
            ])
          )}
        </Grid>
        <Grid item xs={2}>
          {index < list.length - 1
            ? null
            : addRenderer(item, index, list, event =>
                onChange([...list, defaultValue])
              )}
          {index < list.length - 1 || list.length <= 1
            ? null
            : removeRenderer(item, index, list, event =>
                onChange(list.slice(0, -1))
              )}
        </Grid>
      </Grid>
    ))}
  </Fragment>
)

ListEditor.propTypes = {
  classes: PropTypes.object,
  list: PropTypes.array.isRequired,
  onChange: PropTypes.func.isRequired,
  itemRenderer: PropTypes.func.isRequired,
  addRenderer: PropTypes.func.isRequired,
  removeRenderer: PropTypes.func.isRequired,
  defaultValue: PropTypes.any.isRequired
}

export default withStyles(styles)(ListEditor)
