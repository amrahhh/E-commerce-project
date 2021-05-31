const dropCart = document.getElementById('cartdrop');
let qiymet = 0
let basketCount = 0
async function dropCartItem() {
    let response = await fetch('http://localhost:8000/az/api/v1/checkout/order-item/')
    let data = await response.json()
    data.forEach(element => {
        dropCart.innerHTML += `
        <div id="sil${element.id}" class="sin-itme clearfix" data-id="${element.product.id}">
            <i class="mdi mdi-close delete-event" onclick="deleteMethod(this)" id="delete${element.id}" data-id="${element.id}"></i>
            <a class="cart-img" href="{% url 'checkout:cart' %}"><img
                    src="${element.product.main_image}" alt="" /></a>
            <div class="menu-cart-text">
                <a href="#">
                    <h5>${element.product.title}</h5>
                </a>
                <span>Color : ${element.product.color}</span>
                <span>Size : ${element.product.size}</span>
                <strong>$ ${element.product.set_discount_price}</strong>
            </div>
        </div>
    `
        basketCount +=1
        document.getElementById("total-count").innerText = basketCount
    qiymet += parseInt(element.product.set_discount_price) * element.quantity
    document.getElementById("umumi-qiymet").innerHTML = qiymet
    document.getElementById("total-price").innerText = qiymet
    });
}

addLoadEvent(async () => {
    await dropCartItem();
});