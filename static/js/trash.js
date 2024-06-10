function update_total_price() {
    let inputs = document.getElementsByClassName('prod-select-count')

    let total_price = 0

    for (let i=0; i<inputs.length; i++) {
        total_price += parseFloat(inputs[i].getAttribute('data-bs-price')) * inputs[i].value
    }

    document.getElementById('total-sum').innerHTML = 'Итого: ' + total_price

}


function remove_from_trash(pid) {

    let xhr = new XMLHttpRequest()
    xhr.open('POST', '/remove_from_trash', true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = 'json'

    xhr.onload = () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById(`product-${pid}`).remove()
        }
    }

    xhr.send(`pid=${pid}`)

}


function send_order() {

    let inputs = document.getElementsByClassName('prod-select-count')

    let dat = new Map

    for (let i=0; i<inputs.length; i++) {
        if (inputs[i].value > 0)
            dat.set(inputs[i].id, inputs[i].value)
    }

    let query = ''

    for (let [key, value] of dat) {
        query += `${key}=${value}&`
    }

    query = query.slice(0, query.length-1)

    let xhr = new XMLHttpRequest()
    xhr.open('POST', '/add_order', true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = 'json'

    xhr.onload = () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            window.location.href = '/'
        }
    }

    xhr.send(query)

}
