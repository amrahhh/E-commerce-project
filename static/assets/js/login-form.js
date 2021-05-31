const loginForm = document.getElementById('login-form')
const domain = 'http://localhost:8000'

//  ----------------  SNACKBAR ----------------------

function myFunction(e) {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar");
    x.innerText = e

    // Add the "show" class to DIV
    x.className = "show";

    // After 3 seconds, remove the show class from DIV
    setTimeout(function () { x.className = x.className.replace("show", ""); }, 3000);
}

//  ----------------  LOGIN FORM ----------------------

loginForm.addEventListener('submit', async function (e) {
    e.preventDefault();
    let formData = {
        username: loginForm.username.value,
        password: loginForm.password.value,
    }

    let response = await fetch(domain + '/az/api/auth/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    });

    let responseData = await response.json()
    if (response.ok) {  
        localStorage.setItem('token', responseData.token);
        window.location.replace('http://localhost:8000/');
        loginForm.username.value = '';
        loginForm.password.value = '';
        myFunction('Successful...')
    }
    else {
        myFunction('Something went wrong')
    }
});