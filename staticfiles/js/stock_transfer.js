const transferList = [];
const fromDropdown = document.getElementById('fromLocation');
const toDropdown = document.getElementById('toLocation');
const productDropdown = document.getElementById('product');
const locations = ["Lonavala", "Pune", "Pune2", "Nashik", "Girgaon", "Mindgym", "Kharghar"];
const toggle = document.getElementById("toggleDarkMode");

// Populate location options for both 'from' and 'to' dropdowns
function populateLocations() {
  fromDropdown.innerHTML = toDropdown.innerHTML = '<option value="">Select</option>';
  locations.forEach(loc => {
    const opt = `<option value="${loc}">${loc}</option>`;
    fromDropdown.innerHTML += opt;
    toDropdown.innerHTML += opt;
  });
}

// Add a product to the transfer list and update the table
function addProduct() {
  const product = productDropdown.value;
  const quantity = parseInt(document.getElementById("quantity").value);
  const cost = parseFloat(productDropdown.selectedOptions[0].getAttribute("data-cost"));
  const availableStock = parseInt(productDropdown.selectedOptions[0].getAttribute("data-stock"));

  if (!product || quantity <= 0 || quantity > availableStock) {
    alert("Check product and quantity.");
    return;
  }

  transferList.push({ product, quantity, cost });
  updateTable();
  document.getElementById("quantity").value = "";
}

// Update the table with current transfer list
function updateTable() {
  const tbody = document.querySelector("#transferTable tbody");
  tbody.innerHTML = "";
  transferList.forEach((item, i) => {
    tbody.innerHTML += `
      <tr>
        <td>${item.product}</td>
        <td>${item.quantity}</td>
        <td>₹${item.cost}</td>
        <td>₹${item.cost * item.quantity}</td>
        <td><button onclick="removeProduct(${i})">Delete</button></td>
      </tr>
    `;
  });
}

// Remove a product from the transfer list
function removeProduct(i) {
  transferList.splice(i, 1);
  updateTable();
}

// Reset the form to its initial state
function resetForm() {
  fromDropdown.value = "";
  toDropdown.value = "";
  productDropdown.innerHTML = "";
  transferList.length = 0;
  updateTable();
}

// Get CSRF token from cookies
function getCookie(name) {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match ? match[2] : null;
}

// Handle the stock transfer operation
function transferStock() {
  if (!fromDropdown.value || !toDropdown.value || fromDropdown.value === toDropdown.value) {
    alert("Invalid locations");
    return;
  }
  if (!transferList.length) {
    alert("No products to transfer");
    return;
  }

  fetch("/transfer-stock/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken")
    },
    body: JSON.stringify({
      from_location: fromDropdown.value,
      to_location: toDropdown.value,
      items: transferList
    })
  })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        alert("Transfer successful");
        resetForm();
      } else {
        alert("Error: " + data.error);
      }
    });
}

// Handle location change and load available products
fromDropdown.addEventListener("change", () => {
  const loc = fromDropdown.value;
  productDropdown.innerHTML = "<option>Loading...</option>";
  fetch("/api/available-products/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken")
    },
    body: JSON.stringify({ location: loc })
  })
    .then(res => res.json())
    .then(data => {
      productDropdown.innerHTML = '<option value="">Select Product</option>';
      data.products.forEach(p => {
        productDropdown.innerHTML += `<option value="${p.name}" data-cost="${p.cost}" data-stock="${p.quantity}">${p.name} - ₹${p.cost} (Available: ${p.quantity})</option>`;
      });
    });
});

// Toggle dark mode and update the icon
toggle.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  const isDark = document.body.classList.contains("dark-mode");
  localStorage.setItem("theme", isDark ? "dark" : "light");
  toggle.textContent = isDark ? "☀️" : "🌙";
});

// Set theme based on local storage on page load and update the icon accordingly
window.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
  }
  toggle.textContent = document.body.classList.contains("dark-mode") ? "☀️" : "🌙";

  // Populate location dropdowns when the page loads
  populateLocations();
});

// Toggle sidebar visibility
function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("collapsed");

  const btn = document.querySelector(".toggle-sidebar");
  btn.style.left = sidebar.classList.contains("collapsed") ? '1rem' : '240px';
}
