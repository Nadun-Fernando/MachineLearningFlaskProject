document.getElementById("getUrlButton").addEventListener("click", () => {
  chrome.runtime.sendMessage({ action: "getURL" }, (response) => {
    document.getElementById("output").innerText = response.message;
  });
});