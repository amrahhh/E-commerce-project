async function deleteMethod(element) {
    let productId = element.dataset.id
    let response = await fetch(`http://localhost:8000/az/api/v1/checkout/order-item/${productId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${localStorage.getItem('token')}`
        },
        body: JSON.stringify()
    })
    if (response.ok){
        element.parentElement.remove()
        document.getElementById(`remove${productId}`).remove()
    }else{
        alert(response.statusText)
    }
}



async function removeMethod(element) {
    let productId = element.dataset.id
    let response = await fetch(`http://localhost:8000/az/api/v1/checkout/order-item/${productId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${localStorage.getItem('token')}`
        },
        body: JSON.stringify()
    })
    if (response.ok){
        document.getElementById(`remove${productId}`).remove()
        document.getElementById(`sil${productId}`).remove()
    }else{
        alert(response.statusText)
    }
}
