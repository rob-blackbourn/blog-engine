import CONFIG from "../config"

export function register(
  primaryEmail,
  password,
  secondaryEmails,
  givenNames,
  familyName,
  nickname,
  onError,
  onSuccess
) {
  const body = {
    query: `
mutation RegisterUser($primaryEmail: String!, $password: String!, $secondaryEmails: [String], $givenNames: [String], $familyName: String, $nickname: String) {
  registerUser(primaryEmail: $primaryEmail, password: $password, secondaryEmails: $secondaryEmails, givenNames: $givenNames, familyName: $familyName, nickname: $nickname) {
    token
  }
}`,
    variables: {
      primaryEmail,
      password,
      secondaryEmails: secondaryEmails
        .map(x => x.trim())
        .filter(x => x.length > 0),
      givenNames: givenNames.map(x => x.trim()).filter(x => x.length > 0),
      familyName,
      nickname
    }
  }

  const text = JSON.stringify(body)

  fetch(CONFIG.url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json"
    },
    body: text
  })
    .then(response => response.json())
    .then(response => {
      console.log(response)
      if (response.errors) {
        onError(response.errors)
      } else {
        onSuccess(response.data.registerUser.token)
      }
    })
    .catch(error => {
      onError(error)
    })
}

export function login(email, password, onError, onSuccess) {
  const query = `
  mutation Authenticate($email: String!, $password: String!) {
    authenticate(primaryEmail: $email, password: $password) {
      token
    }
  }`

  fetch(CONFIG.url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json"
    },
    body: JSON.stringify({
      query,
      variables: { email, password }
    })
  })
    .then(response => response.json())
    .then(response => {
      if (response.errors) {
        onError(response.errors)
      } else {
        onSuccess(response.data.authenticate.token)
      }
    })
    .catch(error => {
      onError(error)
    })
}
