if (Notification.permission !== "granted") {
    Notification.requestPermission()
}

const status_span = document.querySelector("#status")
const msg_board = document.querySelector("#msgs")
const ws = new WebSocket(`ws://${location.host}/ws`)

ws.addEventListener('open', (e) => {
    console.log("opened")
    status_span.classList = ['ok']
})
ws.addEventListener('message', (e) => {
    console.log(new Notification(e.data))
    const new_msg = document.createElement("div")
    new_msg.innerHTML = 
    `
    <span class="date">${new Date().toISOString()}:</span> <span class="msg">${e.data}</span>
    `
    msg_board.appendChild(new_msg)
})
ws.addEventListener('error', (e) => console.log(e))

console.log("Hello")
