async function fetchBitcoinPrice() {
    const response = await fetch("http://localhost:5000/price"); // We'll set this up next
    const data = await response.json();
    document.getElementById("price").textContent = `$${data.price}`;
}

// Update every 5 seconds
setInterval(fetchBitcoinPrice, 5000);
fetchBitcoinPrice(); // Initial fetch