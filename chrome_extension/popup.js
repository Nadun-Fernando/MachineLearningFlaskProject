document.getElementById('sendUrlButton').addEventListener('click', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const currentUrl = tabs[0].url;
    const flaskAppUrl = 'http://127.0.0.1:5000'; // Replace with your Flask app URL
    const targetUrl = `${flaskAppUrl}?url=${encodeURIComponent(currentUrl)}`;

    // Open a new window to display the Flask app results
    window.open(targetUrl, '_blank');
  });
});