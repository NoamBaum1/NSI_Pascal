function verifierCode() {

    let code = document.getElementById("codeInput").value;
    let message = document.getElementById("message");
    let videoBox = document.getElementById("videoBox");

    if (code === "0119942005") {
        message.style.color = "lightgreen";
        message.textContent = "Code correct ";

        videoBox.classList.remove("hidden");

    } else {
        message.style.color = "red";
        message.textContent = "Code incorrect ";
        videoBox.classList.add("hidden");
    }
}