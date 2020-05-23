function price_update() {
    var price1 = parseInt(document.getElementById('price1').value);
    var price2 = parseInt(document.getElementById('price2').value);
    var shipping = parseInt(document.getElementById('shipping').value);
    var dp = parseInt(document.getElementById('dp').value);
    document.getElementById('vat').value = ((shipping + price1 + price2 + dp) * 0.13).toFixed(2);
    document.getElementById('total').value = ((shipping+ price1 + price2 + dp) * 1.13).toFixed(2);
}

function discount() {
    var discount_code = document.getElementById('discount')
    if (discount_code.value === 'discount') {
        var price1 = parseInt(document.getElementById('price1').value);
        var price2 = parseInt(document.getElementById('price2').value);
        document.getElementById('dp').value = -(price1 + price2) * 0.3;
        discount_disable();
        price_update();
    } else {
        alert("Wrong Discount Code!");
    }
}

function shipping_update1() {
    document.getElementById('shipping').value = 0;
    price_update();
}

function shipping_update2() {
    document.getElementById('shipping').value = 5;
    price_update();
}

function shipping_update3() {
    document.getElementById('shipping').value = 10;
    price_update();
}

function discount_disable() {
    var btn = document.getElementById("discount-btn");
    btn.disabled = true;
}