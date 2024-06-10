function add_to_card(product_id) {

    let xhr = new XMLHttpRequest()
    xhr.open('GET', '/add_to_trash/' + product_id)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = 'json'

    xhr.onload = () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            let button = document.getElementById(`prod-${product_id}`)
            button.innerHTML = '<span>✔</span>'
        }
    }

    xhr.send()

}
