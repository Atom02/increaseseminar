export function setPageTransition (state, data) {
  if (data === 'f') {
    state.enter = 'animated slideInRight faster'
    state.leave = 'animated slideOutLeft faster'
  } else {
    state.enter = 'animated slideInLeft faster'
    state.leave = 'animated slideOutRight faster'
  }
}

export function setHistCount (state, data) {
  if (data.direction === 'f') {
    state.histCounter = parseInt(state.histCounter) + 1
  } else {
    state.histCounter = parseInt(state.histCounter) - 1
  }
  state.lastRoute = data.route
  // state.histCounter = 0
}
