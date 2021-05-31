const updateBtn = document.getElementsByClassName('update-cart')
for (var i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', async function (e) {
        e.preventDefault()
        var productId = this.dataset.product
        inputValue = 1
        let basketData = {
            product: productId,
            quantity: inputValue
        }
        let response = await fetch('http://localhost:8000/az/api/v1/checkout/order-item/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('token')}`
            },
            body: JSON.stringify(basketData)

        })
        data = await response.json()
        let value = data.quantity
        let inputElement = document.querySelector(`[data-id="${data.product.id}"]`)
        if (inputElement) {
            inputElement.value = value;
            return true;
        }
        let response2 = await fetch(`http://localhost:8000/az/api/product/${productId}`)
        data2 = await response2.json();
        console.log(document.getElementById('umumi-qiymet').innerHTML)
        value = parseInt(document.getElementById('umumi-qiymet').innerHTML)
        value += parseInt(data2['set_discount_price']) 
        document.getElementById('umumi-qiymet').innerHTML =  value
        document.getElementById("total-price").innerText = value

        let repeatItem = document.getElementsByClassName('clearfix')
        for (var i = 0; i < repeatItem.length; i++) {
            let repeat = repeatItem[i].getAttribute('data-id')
            if (repeat == productId) {
                let quant = parseInt(data["quantity"])
                quant+=1
                
                return;
            }}
            let dropCart2 = document.getElementById('cartdrop');
            dropCart2.innerHTML += `
            <div class="sin-itme clearfix" data-id="${data2['id']}">
                <i class="mdi mdi-close delete-event" onclick="deleteMethod(this)" id="delete${data2['id']}" data-id="${data2['id']}"></i>
                <a class="cart-img" href="{% url 'checkout:cart' %}"><img
                        src="${data2['main_image']}" alt="" /></a>
                <div class="menu-cart-text">
                    <a href="#">
                        <h5>${data2["title"]}</h5>
                    </a>
                    <span>Color : ${data2["color"]}</span>
                    <span>Size : ${data2["size"]}</span>
                    <strong>$ ${data2["set_discount_price"]}</strong>
                    <span>Size : ${data2["size"]}</span>
                </div>
            </div>
            `
            let basketCounts = parseInt(document.getElementById("total-count").innerText)
            basketCounts +=1
            document.getElementById("total-count").innerText = basketCounts
        })
    }
    