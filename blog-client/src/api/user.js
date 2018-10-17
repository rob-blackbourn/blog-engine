import CONFIG from "../config"

export function currentUser(token, onError, onSuccess) {
  fetch(CONFIG.url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify({
      query: `
query {
  currentUser {
    primaryEmail
    secondaryEmails
    givenNames
    familyName
    nickname
    roles
  }
}`
    })
  })
    .then(response => response.json())
    .then(response => {
      console.log(response)
      if (response.errors) {
        onError(response.errors)
      } else {
        onSuccess(token, response.data.currentUser)
      }
    })
    .catch(error => {
      onError(error)
    })
}
