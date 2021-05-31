const cartList = document.getElementById('cartList')

async function getBacketItem() {
    let response = await fetch('http://localhost:8000/az/api/v1/checkout/order-item/')
    let data = await response.json()
    data.forEach(element => {
        cartList.innerHTML += `
    <tr id="remove${element.id}">
        <td class="td-img text-left">
            <a href="#"><img src="${element.product.image[0].image}" alt="Add Product" /></a>
            <div class="items-dsc">
                <h5><a href="#">${element.product.title}</a></h5>
                <p class="itemcolor">Color: <span>${element.product.color}</span></p>
                <p class="itemcolor">Size: <span>${element.product.size}</span></p>
            </div>
        </td>
        <td>$ <span id="value${element.product.id}">${element.product.set_discount_price}</span></td>
        <td>
            <form action="#" method="POST">
                <div class="plus-minus">
                    <a class="dec qtybutton" data-id="${element.product.id}" onclick=minusFunction(${element.product.id},${element.id}) id='minus'>-</a>
                    <input type="text" value="${element.quantity}" id='count${element.product.id}' name="qtybutton" class="plus-minus-box">
                    <a class="inc qtybutton" data-id="${element.product.id}" onclick=plusFunction(${element.product.id}) id='plus'>+</a>
                </div>
            </form>
        </td>
        <td>
            <strong id='countProd${element.product.id}'>${element.get_total_price}</strong><span>$</span> 
        </td>
        <td class='remove'><i class="mdi mdi-close delete-event" onclick="removeMethod(this)" data-id="${element.id}" id="delete${element.id}" title="Remove this product"></i></td>
    </tr>    
    `
    });
}

addLoadEvent(async () => {
    await getBacketItem()
});


async function minusFunction(productId, elementId) {
    console.log(elementId)
    let element = document.querySelector(`[data-id="${productId}"]`)
    let inputVal = document.getElementById(`count${productId}`).value
    let inputValue = document.getElementById(`count${productId}`).value
    minusEl = parseInt(document.getElementById(`countProd${productId}`).innerText) - (parseInt(document.getElementById(`countProd${productId}`).innerText)) / inputVal
    document.getElementById(`countProd${productId}`).innerText = minusEl
    if (parseInt(document.getElementById(`count${productId}`).value) > 1) {
        inputVal = 2
        document.getElementById(`count${productId}`).value = parseInt(document.getElementById(`count${productId}`).value) - 1
        let minus = {
            product: productId,
            quantity: inputVal
        }
        let response = await fetch('http://localhost:8000/az/api/v1/checkout/order-item/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('token')}`
            },
            body: JSON.stringify(minus)

        })
        document.getElementById("umumi-qiymet").innerHTML = parseInt(document.getElementById("umumi-qiymet").innerHTML) - parseInt(document.getElementById(`value${productId}`).innerText)
        document.getElementById("total-price").innerText = parseInt(document.getElementById("total-price").innerHTML) - parseInt(document.getElementById(`value${productId}`).innerText)
    } else {
        let elementId2 = (elementId)
        let response2 = await fetch(`http://localhost:8000/az/api/v1/checkout/order-item/${elementId2}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('token')}`
            },
            body: JSON.stringify()

        })
        if (response2.ok) {
            removeEl = document.getElementById(`remove${elementId2}`)
            document.getElementById(`sil${elementId2}`).remove()
            removeEl.remove()
        }
    }

}

async function plusFunction(productId) {
    let element = document.querySelector(`[data-id="${productId}"]`)
    let inputVal = document.getElementById(`count${productId}`).value
    let inputValue = document.getElementById(`count${productId}`).value
    plusEl = parseInt(document.getElementById(`countProd${productId}`).innerText) + (parseInt(document.getElementById(`countProd${productId}`).innerText)) / inputVal
    document.getElementById(`countProd${productId}`).innerText = plusEl
    inputVal = 1
    document.getElementById(`count${productId}`).value = parseInt(document.getElementById(`count${productId}`).value) + 1
    let plus = {
        product: productId,
        quantity: inputVal
    }
    let response = await fetch('http://localhost:8000/az/api/v1/checkout/order-item/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${localStorage.getItem('token')}`
        },
        body: JSON.stringify(plus)
    })
    document.getElementById("umumi-qiymet").innerHTML = parseInt(document.getElementById("umumi-qiymet").innerHTML) + parseInt(document.getElementById(`value${productId}`).innerText)
    document.getElementById("total-price").innerText = parseInt(document.getElementById("total-price").innerHTML) + parseInt(document.getElementById(`value${productId}`).innerText)
}

