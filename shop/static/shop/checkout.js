console.log("imported");

if (localStorage.getItem('cart') == null) {
        var cart = {};
    }
    else {
        cart = JSON.parse(localStorage.getItem('cart'));
    }
    var cart_total = 0;
    for (product in cart) {
        let title = cart[product]['title'];
        let amount = cart[product]['amount'];
        let price = cart[product]['price'];
        let image = cart[product]['image'];
        let total = (parseFloat(price) * parseInt(amount));
        cart_total += total;
        item = `
        <li class="list-group-item border">
            <div class="row">
                <div class="col-md-1">
                    <img src="${image}" height="50px">
                </div>
                <div class="checkout-title col-md-9">
                    ${title}
                </div>
                <div class="col-md-2 d-flex justify-content-between align-items-center">
                    <span class="price badge badge-pill badge-light">
                        $${price} x ${amount}
                    </span>
                     <span class="total badge badge-pill badge-info">
                        $${total}
                    </span>
                </div>
            </div>
        </li>`

        $('#product_list').append(item);
    }
    total_price = `
    <li class="list-group-item d-flex justify-content-between align-items-center">
        <b>Your total: </b>
        <span class="total badge badge-pill badge-warning">
            $${cart_total}
        </span>
    </li>
    `
    $('#product_list').append(total_price);
    $('#items').val(JSON.stringify(cart));
    $('#total').val(cart_total);