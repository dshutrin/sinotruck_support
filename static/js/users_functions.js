function rm_user(user_id) {

    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/users/' + user_id + '/delete', true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.responseType = 'json'

    xhr.onload = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            window.location.reload();
        }
    }

    xhr.send()

}

function show_confirm_delete_user_modal(user_id) {
    let modal = document.getElementById("user_modal");
    let modal_text = document.getElementById("modal-text");
    let confirm_button = document.getElementById("confirm_rm_user");

    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/users/' + user_id, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.responseType = 'json'

    xhr.onload = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            modal_text.innerText = `Вы действительно хотите удалить пользователя ${xhr.response['username']}?`
            confirm_button.setAttribute('onclick', `rm_user(${user_id})`)
            modal.style.display = 'flex'
        }
    }

    xhr.send()
}
