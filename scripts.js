// Get the modal
var modal = document.getElementById("add-item-modal");

// Get the button that opens the modal
var btn = document.getElementById("add-item-btn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close-btn")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


// Function to handle cart blinking and hover details
function updateCartStatus(cartItems) {
    const cartElement = document.querySelector('.menu-inner > ul > li:nth-child(5)'); // Assuming Cart is the 5th item
    if (cartItems.length > 0) {
        cartElement.classList.add('blink');
        const cartItemsContainer = document.createElement('div');
        cartItemsContainer.className = 'cart-items';

        let totalPrice = 0;
        cartItems.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.textContent = `${item.name}: $${item.price}`;
            cartItemsContainer.appendChild(itemElement);
            totalPrice += item.price;
        });

        const totalPriceElement = document.createElement('div');
        totalPriceElement.className = 'total-price';
        totalPriceElement.textContent = `Total: $${totalPrice.toFixed(2)}`;
        cartItemsContainer.appendChild(totalPriceElement);

        cartElement.appendChild(cartItemsContainer);
    } else {
        cartElement.classList.remove('blink');
    }
}

// Example usage
const cartItems = [
    { name: 'Apple', price: 1.99 },
    { name: 'Banana', price: 0.99 }
];
updateCartStatus(cartItems);