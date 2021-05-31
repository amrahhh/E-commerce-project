//  ---------------- LOG OUT ----------------------

const logout = document.getElementById('log_out');

logout.addEventListener('click', async function (){
    let response = await fetch('http://localhost:8000/en/logout/' ,{
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
     });
        localStorage.removeItem('token');
        window.location.replace("http://localhost:8000")
});