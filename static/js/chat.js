function sendMessage() {
    let text = document.getElementById("message-text").value;
    let from = document.getElementById("from").value;
    let to = document.getElementById("to").value;
    let body = document.getElementById("messages-body");

    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/chat/messages/add", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = 'json'

    xhr.onload = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {

            body.innerHTML += `
                <div class="my_message">
                    <div class="message">
                        <div class="message-body">
                            <span>${xhr.response['text']}</span>
                        </div>
                        <div class="message-info">
                            <span>Вы: ${xhr.response['date']}</span>
                        </div>
                    </div>
                </div>
            `

            document.getElementById("message-text").value = ""
        }
    }

    xhr.send(`from=${from}&to=${to}&text=${text}`);
}