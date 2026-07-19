async function sendMessage() {

    let input = document.getElementById("user-input");
    let message = input.value;

    if (message.trim() === "") {
        return;
    }

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += "<p><b>You:</b> " + message + "</p>";

    let response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    let data = await response.json();

    chatBox.innerHTML += "<p><b>Bot:</b> " + data.reply + "</p>";

    chatBox.scrollTop = chatBox.scrollHeight;

    input.value = "";
}