function change_price(price, price_id) {
    var extra_price = document.getElementById(price_id);
    var total = document.getElementById("total");
    current = parseFloat(total.innerHTML);
    if (extra_price.value == "0.00") {
        extra_price.value = price;
        let newPrice = current + parseFloat(price);
        newPrice = newPrice.toFixed(2);
        total.innerHTML = newPrice.toString();
    }
    else {
        extra_price.value = "0.00";
        let newPrice = current - parseFloat(price);
        newPrice = newPrice.toFixed(2);
        total.innerHTML = newPrice.toString();
    }
}

