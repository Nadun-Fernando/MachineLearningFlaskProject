chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "getURL") {
        const currentURL = window.location.href;
        fetch("http://localhost:5000/classify", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ url: currentURL }),
        })
            .then((response) => response.json())
            .then((data) => console.log(data));
    }
});