// Ensure you include this script in your HTML file using <script src="app.js"></script>

document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.querySelector('.send-btn');
    const chatInput = document.querySelector('.chat-input input');
    const chatContent = document.querySelector('.chat-content');

    sendButton.addEventListener('click', () => {
        handleUserMessage(chatInput.value);
        chatInput.value = '';  // Clear input after sending
    });

    chatInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            handleUserMessage(chatInput.value);
            chatInput.value = '';  // Clear input after sending
        }
    });

    function handleUserMessage(message) {
        if (!message.trim()) return;  // Don't process empty messages

        addMessageToChat('user', message);

        // Simulate a delay before bot responds
        setTimeout(() => {
            fetchBotResponse(message);
        }, 1000);
    }

    function addMessageToChat(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('chat-message');

        if (sender === 'user') {
            messageElement.innerHTML = `<div class="message-header">You</div><div class="message-body">${message}</div>`;
        } else {
            messageElement.innerHTML = `<div class="message-header">NayayBOT</div><div class="message-body">${message}</div>`;
        }

        chatContent.appendChild(messageElement);
        chatContent.scrollTop = chatContent.scrollHeight;  // Scroll to bottom
    }

    function fetchBotResponse(query) {
        // Simulating web scraping using axios and cheerio (you'd normally run this on the server-side)
        const axios = require('axios');
        const cheerio = require('cheerio');

        // Define the scraping function
        async function scrapeData(query) {
            try {
                const response = await axios.get(`https://example.com/search?q=${encodeURIComponent(query)}`);
                const html = response.data;
                const $ = cheerio.load(html);

                // Extracting specific data, this is just an example. Customize based on your scraping needs.
                const result = $('div.result').first().text().trim();

                addMessageToChat('bot', result || 'Sorry, I could not find any information.');
            } catch (error) {
                console.error('Error fetching data:', error);
                addMessageToChat('bot', 'Sorry, something went wrong while processing your request.');
            }
        }

        scrapeData(query);
    }
});
