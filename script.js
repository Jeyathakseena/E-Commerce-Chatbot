// Select elements
const chatIcon = document.getElementById("chat-icon");
const chatContainer = document.getElementById("chat-container");
const closeBtn = document.getElementById("close-btn");
const sendBtn = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");
const chatContent = document.getElementById("chat-content");

// Toggle Chat Container Visibility
chatIcon.addEventListener("click", () => {
    chatContainer.classList.toggle("hidden");
});

closeBtn.addEventListener("click", () => {
    chatContainer.classList.add("hidden");
});

// Function to send a message
function sendMessage() {
    const message = userInput.value.trim();
    if (message === "") return;

    // Add user's message
    appendMessage("user-message", message);

    // Clear input
    userInput.value = "";

    // Fetch response from Flask backend
    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: message }),
    })
    .then(response => response.json())
    .then(data => {
        // Add bot's response with line breaks
        appendMessage("bot-message", data.response.replace(/\n/g, "<br>"));
    })
    .catch(error => {
        console.error("Error:", error);
        appendMessage("bot-message", "Sorry, something went wrong. Please try again.");
    });
}

// Helper Function to Append Messages
function appendMessage(className, message) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add(className);
    messageDiv.innerHTML = message; // Use innerHTML to render <br> tags
    chatContent.appendChild(messageDiv);
    chatContent.scrollTop = chatContent.scrollHeight;
}

// Event listener for send button
sendBtn.addEventListener("click", sendMessage);

// Event listener for Enter key
userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});

