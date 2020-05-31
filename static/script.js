function store_info() {
    var x1 = document.getElementById("select1").selectedIndex;
    var y1 = document.getElementById("select1").options;
    var x2 = document.getElementById("select2").selectedIndex;
    var y2 = document.getElementById("select2").options;
    localStorage.product_storage1 = y1[x1].index;
    localStorage.product_storage2 = y2[x2].index;
    var radios = document.getElementsByName("radio-shipping");
    for(var i=0;i<radios.length;i++){
        if (radios[i].checked === true){
            localStorage.radio_storage = radios[i].id
            break;
        }
    }
}

function load_info() {
    if (localStorage.product_storage1 != null && localStorage.product_storage2 != null) {
        document.getElementById('select1').options[localStorage.getItem('product_storage1')].selected = true;
        document.getElementById('select2').options[localStorage.getItem('product_storage2')].selected = true;
    }
    if (localStorage.radio_storage != null) {
        var radios = document.getElementsByName("radio-shipping");
        var val = localStorage.getItem('radio_storage');
        console.log(val);
        for(var i=0;i<radios.length;i++){
            if (radios[i].id === val){
                radios[i].checked = true;
                break;
            }
        }
    }
}

function click_modify() {
    document.getElementById('modify').click()
}

function first_load() {
    if (window.location.pathname === '/') {
        load_info()
        click_modify()
    }
}

function price_update() {
    var price1 = parseInt(document.getElementById('num1').value);
    var price2 = parseInt(document.getElementById('num2').value);
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

function discount_disable() {
    var btn = document.getElementById("discount-btn");
    btn.disabled = true;
}