function click_action(uid) {

    let el = document.getElementById('user-' + uid)

    if (el.classList.contains('selected')) {
        el.classList.remove('selected')
    } else {
        el.classList.add('selected')
    }
}

function update_all(class_, cb) {
    let elems = document.getElementsByClassName(class_)
    if (document.getElementById(cb).checked === true) {
        for (let i = 0; i < elems.length; i++) {
            document.getElementById(elems[i].id).classList.add('selected')
        }
    } else {
        for (let i = 0; i < elems.length; i++) {
            document.getElementById(elems[i].id).classList.remove('selected')
        }
    }
}
