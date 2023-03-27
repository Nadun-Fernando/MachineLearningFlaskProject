chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getURL") {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      const currentURL = tabs[0].url;
      fetch("http://localhost:5000/classify", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: currentURL }),
      })
        .then((response) => response.json())
        .then((data) => {
          sendResponse({ message: `Flask response: ${data.result}` });
        })
        .catch((error) => {
          console.error("Error:", error);
          sendResponse({ message: "Error: Unable to reach Flask server." });
        });
    });
  }
  return true; // Required for async sendResponse
});