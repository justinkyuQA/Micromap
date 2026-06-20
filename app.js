document
.getElementById("scanBtn")
.addEventListener("click", () => {

    alert(
        "MicroMap v0.1\n\nNetwork scan coming in v0.2"
    );

});

if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register(
        'service-worker.js'
    );
}
