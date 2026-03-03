//module
const users = fetch ('https://jsonplaceholder.typicode.com/users')
.then(response => response.json())
.catch(err =>console.log(err));

//.then (data => data.value)

export default users;