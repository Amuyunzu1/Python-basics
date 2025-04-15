let cart = {};

function addToCart(item) {
    if (cart[item]) {
        cart[item] += 1; // Increase item count if already in cart
    } else {
        cart[item] = 1; // Add new item to cart
    }
    updateCartCount();
}

function removeFromCart(item) {
    if (cart[item]) {
        cart[item] -= 1; // Decrease item count
        if (cart[item] === 0) {
            delete cart[item]; // Remove item if count is 0
        }
    }
    updateCartCount();
}

function updateCartCount() {
    let totalCount = 0;
    for (let item in cart) {
        totalCount += cart[item];
    }
    document.getElementById('count').innerText = totalCount;
}