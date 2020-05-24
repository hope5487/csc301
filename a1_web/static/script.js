function store_info() {
    var x1 = document.getElementById("num1").selectedIndex;
    var y1 = document.getElementById("num1").options;
    var x2 = document.getElementById("num2").selectedIndex;
    var y2 = document.getElementById("num2").options;
    localStorage.product1 = y1[x1].index;
    localStorage.product2 = y2[x2].index;
}

function load_info() {
    if (localStorage.product1 != null && localStorage.product2 != null) {
        document.getElementById('num1').options[localStorage.getItem('product1')].selected = true;
        document.getElementById('num2').options[localStorage.getItem('product2')].selected = true;
    }
}

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