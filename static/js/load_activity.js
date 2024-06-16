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

function load_act() {
    let els = document.getElementsByClassName('selected')
    let query = ''
    for (let i=0; i < els.length; i++) {
        let id = els[i].id.replace('user-', '')
        query += `id${id}=${id}&`
    }

    let start = document.getElementById('sdate').value
    let end = document.getElementById('edate').value
    query += `start=${start}&end=${end}`

    let xhr = new XMLHttpRequest()
    xhr.open('POST', '/load_activity', true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = 'json'

    xhr.onload = () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            window.location.href = xhr.response['link']
        }
    }

    xhr.send(query)

}


function search_user() {
    let username = document.getElementById('fau').value

    let users = document.getElementsByClassName('user-activity-link')

    for (let i=0; i<users.length; i++) {

        console.log(users[i].textContent)

        if (!users[i].textContent.includes(username)) {
            users[i].style.display = 'none'
        } else {
            users[i].style.display = 'flex'
        }
    }

}

