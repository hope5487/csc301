function price_update() {
    var price1 = parseInt(document.getElementById('price1').value);
    var price2 = parseInt(document.getElementById('price2').value);
    var total = ((price1 + price2) * 1.13).toFixed(2);
    document.getElementById('total').value = total;
}