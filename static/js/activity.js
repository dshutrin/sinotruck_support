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
