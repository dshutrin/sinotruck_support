function update_my_task() {
    let task = document.getElementById('my_task_input').value

    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/users/update_task", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = 'json'

    xhr.onload = function () {

        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById('my_task').style.backgroundColor = 'lightgreen'
            setTimeout(() => {

                    document.getElementById('my_task').style.backgroundColor = '#212529'

                },
                2000
            );
        }


    }

    xhr.send(`task=${task}`)

}


function update_my_receiver() {

    let value = document.getElementById('receiver').checked

    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/users/update_receiver", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = 'json'

    xhr.onload = function () {

        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById('receiver-block').style.backgroundColor = 'lightgreen'
            setTimeout(
                () => {
                    document.getElementById('receiver-block').style.backgroundColor = '#212529'
                },
                2000
            );
        }


    }

    xhr.send(`value=${value}`)

}
